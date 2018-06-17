from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView

from ask_zinovyev_app.forms import NewQuestionForm
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


class NewQuestionView(LoginRequiredMixin, CreateView):
    form_class = NewQuestionForm
    template_name = 'ask_zinovyev_app/ask.html'

    def form_valid(self, form):
        form.set_user(self.request.user)
        return super().form_valid(form)

    def get_login_url(self):
        return reverse('ask_zinovyev_app/sign_in')

    def get_success_url(self):
        return reverse('ask_zinovyev_app/index')
