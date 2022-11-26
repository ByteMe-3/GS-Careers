from django.urls import path

from .views import (
    LoginView,
    QuizView,
    RegisterView,
    TaskCreateView,
    TaskListView,
    TaskRetrieveView,
    UserProfileView,
)

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("register/", RegisterView.as_view()),
    path("profile/<pk>", UserProfileView.as_view()),
    path("task/list/", TaskListView.as_view()),
    path("task/create/", TaskCreateView.as_view()),
    path("task/<pk>", TaskRetrieveView.as_view()),
    path("quiz/", QuizView.as_view()),
]
