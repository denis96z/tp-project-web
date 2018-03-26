from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET


@require_GET
def index(request):
    return redirect(questions)


@require_GET
def questions(request):
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10000
    paginator = Paginator(lst, 5)
    return render(request, 'ask_zinovyev_app/questions-all.html',
                  {'page': paginator.page(page)})


@require_GET
def ask(request):
    return render(request, 'ask_zinovyev_app/ask.html')


@require_GET
def tag(request):
    return render(request, 'ask_zinovyev_app/questions-by-tag.html')


@require_GET
def question(request):
    return render(request, 'ask_zinovyev_app/question.html')


@require_GET
def register(request):
    return render(request, 'ask_zinovyev_app/register.html')


@require_GET
def login(request):
    return render(request, 'ask_zinovyev_app/login.html')


@require_GET
def settings(request):
    return render(request, 'ask_zinovyev_app/settings.html')