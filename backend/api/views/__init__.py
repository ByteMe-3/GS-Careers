from .login import LoginView
from .register import RegisterView
from .user_profile import UserProfileView
from .task import TaskListView, TaskCreateView, TaskRetrieveView
from .quiz import QuizView

__all__ = ["LoginView", "RegisterView", "UserProfileView", "TaskListView", "TaskCreateView", "TaskRetrieveView", "QuizView"]