from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET

from ask_zinovyev_app.models import Question, Tag


def parse_page(request):
    try:
        p = request.GET.get('page')
        if not (p is None):
            return int(p)
        return 1
    except ValueError:
        raise Http404


def get_order_and_template(ordering):
    if (ordering is None) or ordering == 'recent':
        return '-date_time_added', 'ask_zinovyev_app/recent-questions.html'
    elif ordering == 'popular':
        return '-rating', 'ask_zinovyev_app/popular-questions.html'
    else:
        raise Http404


def get_tag(id):
    try:
        return Tag.objects.get(pk=id)
    except (Tag.DoesNotExist, Tag.MultipleObjectsReturned):
        raise Http404


def get_current_page(objects, index):
    try:
        paginator = Paginator(objects, 20)
        return paginator.page(index)
    except InvalidPage:
        raise Http404


@require_GET
def get_index(request):
    return redirect(get_all_questions, ordering='recent')


@require_GET
def get_all_questions(request, ordering):
    p = parse_page(request)
    order, template = get_order_and_template(ordering)
    questions = Question.objects.filter(is_active=True).order_by(order)
    page_objects = get_current_page(questions, p)
    return render(request, template, {'page': page_objects})


@require_GET
def get_questions_by_tag(request, id):
    p = parse_page(request)
    tag = get_tag(id)
    questions = Question.objects.filter(is_active=True, tags__pk=id)
    page_objects = get_current_page(questions, p)
    return render(request, 'ask_zinovyev_app/questions-by-tag.html', {'tag': tag, 'page': page_objects})


@require_GET
def ask(request):
    return render(request, 'ask_zinovyev_app/ask.html')


@require_GET
def question(request, question_id):
    question_info = Question.objects.filter(publication_ptr_id=question_id)
    if question_info:
        return render(request, 'ask_zinovyev_app/question.html', {'question': question_info})
    else:
        return Http404


@require_GET
def register(request):
    return render(request, 'ask_zinovyev_app/register.html')


@require_GET
def login(request):
    return render(request, 'ask_zinovyev_app/login.html')


@require_GET
def settings(request):
    return render(request, 'ask_zinovyev_app/settings.html')
