from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from ..serializers import QuestionSerializer
from ..models import Question
import json


class QuizView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def post(self, request, *args, **kwargs):
        query_params = request.query_params

        pass



