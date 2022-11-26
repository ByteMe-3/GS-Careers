from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from ..models import Task
from ..serializers import TaskSerializer


class TaskListView(ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskCreateView(CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveView(RetrieveAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
