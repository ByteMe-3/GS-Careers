from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from ..serializers import TaskSerializer
from ..models import Task


class TaskListView(ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskCreateView(CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveView(RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
