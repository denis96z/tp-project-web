from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET

from ask_zinovyev_app.models import Question


@require_GET
def index(request):
    return redirect(all_questions)


@require_GET
def all_questions(request):
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    questions_list = Question.objects.all()
    paginator = Paginator(questions_list, 5)

    try:
        return render(request,
                      'ask_zinovyev_app/questions-all.html',
                      {'page': paginator.page(page)})
    except:
        return Http404


@require_GET
def ask(request):
    return render(request, 'ask_zinovyev_app/ask.html')


@require_GET
def tag(request):
    return render(request, 'ask_zinovyev_app/questions-by-tag.html')


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
