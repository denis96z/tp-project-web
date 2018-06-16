from django.urls import path

from ask_zinovyev_app.views import views
from ask_zinovyev_app.views.index import IndexView
from ask_zinovyev_app.views.question import QuestionView
from ask_zinovyev_app.views.questions import \
    AllQuestionsView, PopularQuestionsView,\
    RecentQuestionsView, QuestionsByTagView

urlpatterns = [
    path('', IndexView.as_view(), name='ask_zinovyev_app/index'),

    path('questions', AllQuestionsView.as_view(), name='ask_zinovyev_app/all_questions'),
    path('questions/popular', PopularQuestionsView.as_view(), name='ask_zinovyev_app/popular_questions'),
    path('questions/recent', RecentQuestionsView.as_view(), name='ask_zinovyev_app/recent_questions'),
    path('questions/tag/<int:tag_id>', QuestionsByTagView.as_view(), name='ask_zinovyev_app/questions_by_tag'),

    path('question/<int:question_id>/answers/new', views.post_answer, name='ask_zinovyev_app/answer'),
    path('question/<int:question_id>', QuestionView.as_view(), name='ask_zinovyev_app/question'),
    path('question/new', views.ask, name='ask_zinovyev_app/ask'),

    path('sign-up', views.sign_up, name='ask_zinovyev_app/sign_up'),
    path('sign-in', views.sign_in, name='ask_zinovyev_app/sign_in'),
    path('sign-out', views.sign_out, name='ask_zinovyev_app/sign_out'),

    path('profile/<int:user_id>', views.view_profile, name='ask_zinovyev_app/profile'),
    path('profile/edit', views.edit_profile, name='ask_zinovyev_app/edit_profile'),
]
