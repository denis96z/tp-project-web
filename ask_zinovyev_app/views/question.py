from django.views.generic import ListView

from ask_zinovyev_app.models import Answer, get_active_or_404, Question


class QuestionView(ListView):
    paginate_by = 10
    template_name = 'ask_zinovyev_app/question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = get_active_or_404(Question, pk=self.kwargs['question_id'])
        return context

    def get_queryset(self):
        return Answer.objects.by_question(self.kwargs['question_id'])
