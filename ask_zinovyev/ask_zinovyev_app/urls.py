from django.urls import path
from ask_zinovyev_app import views


urlpatterns = [
    path('', views.get_index, name='ask_zinovyev_app/index'),

    path('questions', views.get_all_questions, name='ask_zinovyev_app/all_questions'),
    path('questions/popular', views.get_popular_questions, name='ask_zinovyev_app/popular_questions'),
    path('questions/recent', views.get_recent_questions, name='ask_zinovyev_app/recent_questions'),
    path('questions/tag/<int:tag_id>', views.get_questions_by_tag, name='ask_zinovyev_app/questions_by_tag'),

    path('question/<int:question_id>', views.get_question, name='ask_zinovyev_app/question'),
    path('question/ask', views.ask, name='ask_zinovyev_app/ask'),

    path('sign-up', views.register, name='ask_zinovyev_app/sign_up'),
    path('sign-in', views.login, name='ask_zinovyev_app/sign_in'),

    path('profile/<int:user_id>',views.view_profile, name='ask_zinovyev_app/profile'),
    path('profile/edit', views.edit_profile, name='ask_zinovyev_app/edit_profile'),
]
