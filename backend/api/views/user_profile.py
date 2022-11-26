from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView

from ..serializers import UserSerializer
from ..models import UserProfile
from ..serializers import UserProfileSerializer


class UserProfileView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class ChangePointsView(APIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    #def get(self, request, *args, **kwargs):

