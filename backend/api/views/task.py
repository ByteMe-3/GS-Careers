from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView

from ..serializers import TaskSerializer
from ..models import Task

class TaskListView(ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


