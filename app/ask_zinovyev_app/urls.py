from django.urls import path

from ask_zinovyev_app.views import views
from ask_zinovyev_app.views.index import IndexView
from ask_zinovyev_app.views.question import QuestionView, NewQuestionView
from ask_zinovyev_app.views.questions import \
    AllQuestionsView, PopularQuestionsView,\
    RecentQuestionsView, QuestionsByTagView
from ask_zinovyev_app.views.user import SignInView, sign_out, SignUpView

urlpatterns = [
    path('', IndexView.as_view(), name='ask_zinovyev_app/index'),

    path('questions', AllQuestionsView.as_view(), name='ask_zinovyev_app/all_questions'),
    path('questions/popular', PopularQuestionsView.as_view(), name='ask_zinovyev_app/popular_questions'),
    path('questions/recent', RecentQuestionsView.as_view(), name='ask_zinovyev_app/recent_questions'),
    path('questions/tag/<int:tag_id>', QuestionsByTagView.as_view(), name='ask_zinovyev_app/questions_by_tag'),

    path('question/<int:question_id>/answers/new', views.post_answer, name='ask_zinovyev_app/answer'),
    path('question/<int:question_id>', QuestionView.as_view(), name='ask_zinovyev_app/question'),
    path('question/new', NewQuestionView.as_view(), name='ask_zinovyev_app/ask'),

    path('sign-up', SignUpView.as_view(), name='ask_zinovyev_app/sign_up'),
    path('sign-in', SignInView.as_view(), name='ask_zinovyev_app/sign_in'),
    path('sign-out', sign_out, name='ask_zinovyev_app/sign_out'),

    path('profile/<int:user_id>', views.view_profile, name='ask_zinovyev_app/profile'),
    path('profile/edit', views.edit_profile, name='ask_zinovyev_app/edit_profile'),
]
