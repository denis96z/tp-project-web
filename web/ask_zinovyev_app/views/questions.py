from django.shortcuts import get_object_or_404
from django.views.generic import ListView, RedirectView

from ask_zinovyev_app.models import Question, Tag


class QuestionsView(ListView):
    paginate_by = 20


class AllQuestionsView(RedirectView):
    pattern_name = 'ask_zinovyev_app/recent_questions'


class RecentQuestionsView(QuestionsView):
    queryset = Question.objects.recent()
    template_name = 'ask_zinovyev_app/recent-questions.html'


class PopularQuestionsView(QuestionsView):
    queryset = Question.objects.popular()
    template_name = 'ask_zinovyev_app/popular-questions.html'


class QuestionsByTagView(QuestionsView):
    template_name = 'ask_zinovyev_app/questions-by-tag.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, pk=self.kwargs['tag_id'])
        return context

    def get_queryset(self):
        return Question.objects.by_tag(self.kwargs['tag_id'])
