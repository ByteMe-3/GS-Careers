from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import QuestionSerializer
from ..models import Question
import json


class QuizView(APIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class
        data = self.queryset.values('id', 'question', 'answers')

        serializer = serializer(data=list(data), many=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        return Response(data)

    def post(self, request, *args, **kwargs):
        query_params = request.query_params

        pass



