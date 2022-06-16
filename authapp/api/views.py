from django.forms import ValidationError
from rest_framework import viewsets, generics, permissions
from authapp.models import CustomUser
from rest_framework.response import Response
from rest_framework import status

# from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from authapp.serializers import (
    UserSerializer,
    CustomObtainToken,
)
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.conf import settings
from authapp.email_stuff import send_msg


class UserCreateViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.filter(is_active=True)
    pagination_class = None
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user = CustomUser.objects.create_user(
            username=data["username"],
            password=data["password"],
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            # country=valid_data["country"],
        )
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TokenObtainUsernameView(TokenObtainPairView):
    serializer_class = CustomObtainToken


class VerifyEmailToken(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def create(self, request, *args, **kwargs):
        verification_code = request.data.get("verification_code")
        try:
            q = CustomUser.objects.get(email_verification_code=verification_code)
            if q.email_verified:
                return Response(
                    {"response": "E-mail already verified and account was activated"},
                    400,
                )
            q.email_verified = True
            q.save()
            return Response({"response": "E-mail verified"}, status=200)
        # invalid uuid
        except ValidationError:
            raise Http404


class VerifyEmailCodeByClickingLink(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def retrieve(self, *args, **kwargs):
        verification_code = self.kwargs.get("verification_code")
        try:
            q = CustomUser.objects.get(email_verification_code=verification_code)
            if q.email_verified:
                return Response(
                    {"response": "E-mail already verified and account was activated"},
                    400,
                )
            q.email_verified = True
            q.save()
            return Response({"response": "E-mail verified"}, status=200)
        except ValidationError:
            raise Http404


class SendMailView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def create(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, email=request.data.get("email"))
        if user:
            send_msg(
                settings.EMAIL_HOST,
                settings.EMAIL_PORT,
                settings.EMAIL_HOST_USER,
                settings.EMAIL_HOST_PASSWORD,
                request.data.get("email"),
                "Email Verification at El-Shopperino",
                f"Hey, pls activate yo account by clicking here: \n{request.data.get('link')}",
            )
            return Response({"response": "Email has been sent"})
