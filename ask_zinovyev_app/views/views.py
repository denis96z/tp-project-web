from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from ask_zinovyev_app.forms import QuestionForm, AnswerForm, LoginForm
from ask_zinovyev_app.models import Answer, get_active_or_404

PAGINATE_BY = 20


@require_http_methods(['GET', 'POST'])
def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.sign_in(request):
            pass
            # return redirect(get_index)
    return render(request, 'ask_zinovyev_app/login.html', {
        'form': form
    })


@require_http_methods(['GET', 'POST'])
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'ask_zinovyev_app/register.html')
    else:
        raise NotImplementedError


@require_GET
@login_required(redirect_field_name=sign_in)
def sign_out(request):
    logout(request)
    pass
    # return redirect(get_index)


@require_http_methods(['GET', 'POST'])
@login_required(redirect_field_name=sign_in)
def ask(request):
    if request.method == 'GET':
        form = QuestionForm(request.user)
    else:
        form = QuestionForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # return redirect(get_index)
    return render(request, 'ask_zinovyev_app/ask.html', {
        'form': form
    })


@require_GET
def get_question(request, question_id):
    pass
    # p = parse_page(request)
    # q = get_active_or_404(Question, pk=question_id)
    # answers = Answer.objects.by_question(question_id)
    # page_objects = get_current_page(answers, p)
    # return render(request, 'ask_zinovyev_app/question.html', {
    #     'question': q,
    #     'answers': page_objects
    # })


@require_POST
@login_required(redirect_field_name=sign_in)
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
@login_required(redirect_field_name=sign_in)
def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'ask_zinovyev_app/settings.html')
    else:
        raise NotImplementedError
