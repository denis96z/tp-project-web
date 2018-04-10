from django.urls import path
from ask_zinovyev_app import views

urlpatterns = [
    path('', views.get_index, name='ask_zinovyev_app/index'),
    path('questions/<slug:ordering>', views.get_all_questions, name='ask_zinovyev_app/questions'),
    path('tag/<int:id>', views.get_questions_by_tag, name='ask_zinovyev_app/tag'),
    path('question/<int:id>', views.question, name='ask_zinovyev_app/question'),
    path('ask', views.ask, name='ask_zinovyev_app/ask'),
    path('register', views.register, name='ask_zinovyev_app/register'),
    path('login', views.login, name='ask_zinovyev_app/login'),
    path('settings', views.settings, name='ask_zinovyev_app/settings')
]
