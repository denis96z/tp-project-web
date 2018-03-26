from django.core.paginator import Paginator
from django.shortcuts import render, redirect


def index(request):
    return redirect(questions)


def questions(request):
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10000
    paginator = Paginator(lst, 5)
    return render(request, 'ask_zinovyev_app/questions.html',
                  {'page': paginator.page(page)})


def ask(request):
    return render(request, 'ask_zinovyev_app/ask.html')


def tag(request):
    return render(request, 'ask_zinovyev_app/tag.html')


def question(request):
    return render(request, 'ask_zinovyev_app/question.html')


def register(request):
    return render(request, 'ask_zinovyev_app/register.html')


def login(request):
    return render(request, 'ask_zinovyev_app/login.html')


def settings(request):
    return render(request, 'ask_zinovyev_app/settings.html')