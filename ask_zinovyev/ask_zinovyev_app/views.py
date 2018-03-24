from django.shortcuts import render


def index(request):
    return render(request, 'ask_zinovyev_app/questions.html')


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