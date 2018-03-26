from django.urls import path, re_path
from ask_zinovyev_app import views


urlpatterns = [
    path('', views.index, name='ask_zinovyev_app/index'),
    path('questions', views.questions, name='ask_zinovyev_app/questions'),
    re_path(r'^questions/(?P<page>[0-9]{7})/$', views.questions, name='ask_zinovyev_app/questions'),
    path('ask', views.ask, name='ask_zinovyev_app/ask'),
    path('tag', views.tag, name='ask_zinovyev_app/tag'),
    path('question', views.question, name='ask_zinovyev_app/question'),
    path('register', views.register, name='ask_zinovyev_app/register'),
    path('login', views.login, name='ask_zinovyev_app/login'),
    path('settings', views.settings, name='ask_zinovyev_app/settings')
]