from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from ..serializers import QuestionSerializer
from ..models import Question
import json


class QuizView(ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def post(self, request, *args, **kwargs):
        points = 0
        data = request.data
        for question in data:
            question_instance = self.queryset.get(id=question.get("id") )
            for i, answer in enumerate(question_instance.answers):
                if answer == question.get("answer"):
                    points += question_instance.rewards[i]

        result = ""
        if points < 50:
            result = "Risk Engeenering "
        elif points < 40:
            result = "Software Engeneering"
        elif points < 30:
            result = "Data Analyst"
        elif points < 20:
            result = "Cybersecurity Team"
        else:
            result = "Machine Learning"
        return Response(result)



