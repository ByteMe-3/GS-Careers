from rest_framework.response import Response
from rest_framework.views import APIView


class Example(APIView):
    def get(self, request):
        print("Example")
        return Response("X")
