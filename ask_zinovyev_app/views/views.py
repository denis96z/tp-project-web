from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods, require_POST


@require_http_methods(['GET', 'POST'])
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'ask_zinovyev_app/register.html')
    else:
        raise NotImplementedError


@require_POST
@login_required()
def post_answer(request, question_id):
    pass
    # q = get_active_or_404(Question, pk=question_id)
    # form = AnswerForm(request.user, q, request.POST)
    # if form.is_valid():
    #     form.save()
    # return redirect(get_question, question_id)


@require_GET
def view_profile(request, _):
    raise NotImplementedError


@require_http_methods(['GET', 'POST'])
@login_required()
def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'ask_zinovyev_app/settings.html')
    else:
        raise NotImplementedError
