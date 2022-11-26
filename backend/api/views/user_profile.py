from rest_framework.generics import RetrieveAPIView

from ..serializers import UserSerializer
from ..models import UserProfile
from ..serializers import UserProfileSerializer


class UserProfileView(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

