from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.http import require_GET


class SignInView(LoginView):
    template_name = 'ask_zinovyev_app/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        else:
            return reverse('ask_zinovyev_app/index')


@require_GET
@login_required()
def sign_out(request):
    logout(request)
    return redirect(reverse('ask_zinovyev_app/index'))
