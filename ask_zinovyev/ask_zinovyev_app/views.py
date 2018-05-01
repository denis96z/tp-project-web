from django.contrib.auth import logout
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from ask_zinovyev.http import Http401
from ask_zinovyev_app.models import Question, Tag, Answer, get_active_or_404


def parse_page(request):
    try:
        p = request.GET.get('page')
        if not (p is None):
            return int(p)
        return 1
    except ValueError:
        raise Http404


def get_current_page(objects, index):
    try:
        paginator = Paginator(objects, 20)
        return paginator.page(index)
    except InvalidPage:
        raise Http404


@require_GET
def get_index(request):
    return redirect(get_recent_questions)


@require_GET
def get_all_questions(request):
    return redirect(get_recent_questions)


@require_GET
def get_popular_questions(request):
    questions = Question.objects.popular()
    return get_questions(request, questions, 'ask_zinovyev_app/popular-questions.html')


@require_GET
def get_recent_questions(request):
    questions = Question.objects.recent()
    return get_questions(request, questions, 'ask_zinovyev_app/recent-questions.html')


@require_GET
def get_questions_by_tag(request, tag_id):
    p = parse_page(request)
    tag = get_object_or_404(Tag, pk=tag_id)
    questions = Question.objects.by_tag(tag_id)
    page_objects = get_current_page(questions, p)
    return render(request, 'ask_zinovyev_app/questions-by-tag.html', {'tag': tag, 'page': page_objects})


def get_questions(request, questions, template):
    p = get_current_page(questions, parse_page(request))
    return render(request, template, {'page': p})


@require_http_methods(['GET', 'POST'])
def ask(request):
    return render(request, 'ask_zinovyev_app/ask.html')


@require_GET
def get_question(request, question_id):
    p = parse_page(request)
    q = get_active_or_404(Question, pk=question_id)
    answers = Answer.objects.by_question(question_id)
    page_objects = get_current_page(answers, p)
    return render(request, 'ask_zinovyev_app/question.html', {'question': q, 'answers': page_objects})


@require_http_methods(['GET', 'POST'])
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'ask_zinovyev_app/register.html')
    else:
        raise NotImplementedError


@require_http_methods(['GET', 'POST'])
def sign_in(request):
    if request.method == 'GET':
        return render(request, 'ask_zinovyev_app/login.html')
    else:
        raise NotImplementedError


@require_POST
def sign_out(request):
    if not request.user.is_authenticated:
        return Http401
    logout(request)
    return redirect(get_index)


@require_GET
def view_profile(request, user_id):
    if request.method == 'GET':
        return render(request, 'ask_zinovyev_app/layout.html')
    else:
        raise NotImplementedError


@require_http_methods(['GET', 'POST'])
def edit_profile(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return Http401
        return render(request, 'ask_zinovyev_app/settings.html')
    else:
        raise NotImplementedError
