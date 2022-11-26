from .login import LoginView
from .quiz import QuizView
from .register import RegisterView
from .task import TaskCreateView, TaskListView, TaskRetrieveView
from .user_profile import UserProfileView

__all__ = [
    "LoginView",
    "RegisterView",
    "UserProfileView",
    "TaskListView",
    "TaskCreateView",
    "TaskRetrieveView",
    "QuizView",
]
