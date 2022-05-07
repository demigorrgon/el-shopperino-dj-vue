from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User

from authapp.serializers import UserCreateSerializer, UserSerializer


class UserCreateViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserSerializer

        return UserCreateSerializer
