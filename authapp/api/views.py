from rest_framework import viewsets
from rest_framework import permissions
from authapp.models import CustomUser

# from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from authapp.serializers import UserCreateSerializer, UserSerializer, CustomObtainToken

# from django.shortcuts import get_object_or_404


class UserCreateViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.filter(is_active=True)
    pagination_class = None

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer

        return UserCreateSerializer

    # def get_queryset(self):
    #     qs = CustomUser.objects.all()
    #     single_user_id = self.request.query_params.get("id")

    #     if single_user_id:
    #         qs = CustomUser.objects.filter(id=single_user_id)
    # def get_object(self):
    #     if self.kwargs.get("pk"):
    #         obj = self.kwargs.get("pk")
    #         return get_object_or_404(CustomUser, id=obj)


class TokenObtainUsernameView(TokenObtainPairView):
    serializer_class = CustomObtainToken
