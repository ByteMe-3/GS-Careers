from rest_framework.response import Response
from rest_framework.views import APIView
from .create_token import create_token

class Example(APIView):
    def get(self, request):
        print("Example")
        create_token()
        return Response("X")
