from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from ..serializers import UserSerializer
from ..models import UserProfile
from ..email import send_email

class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        send_email()
        serializer = self.serializer_class
        serializer = serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_instance = serializer.save()
        user_profile_instance = UserProfile.objects.get(user=user_instance)

        ref_id = request.query_params.get("ref", None)
        if ref_id:
            try:
                ref_id = request.query_params.get("ref", None)
                ref_user_instance = UserProfile.objects.get(id=ref_id)
                user_profile_instance.ref = ref_user_instance
                user_profile_instance.save()
            except:
                return Response("Couldnt attach referral user")
        return Response(serializer.data)


def admin_logout_view(request):
    logout(request)
    response = redirect("/#")
    response.delete_cookie("token")
    return response
