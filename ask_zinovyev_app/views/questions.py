from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, RedirectView

from ask_zinovyev_app.models import Question, Tag
from ask_zinovyev_app.views.views import PAGINATE_BY


class QuestionsView(ListView):
    paginate_by = PAGINATE_BY


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

    def get_tag(self):
        try:
            return int(self.request.GET['tag_id'])
        except (KeyError, TypeError):
            raise Http404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, pk=self.get_tag())
        return context

    def get_queryset(self):
        return Question.objects.by_tag(self.get_tag())
