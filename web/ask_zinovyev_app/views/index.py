from django.views.generic import RedirectView


class IndexView(RedirectView):
    pattern_name = 'ask_zinovyev_app/all_questions'
