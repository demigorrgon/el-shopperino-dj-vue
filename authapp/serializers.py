from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        )

    def create(self, valid_data):
        user = User.objects.create_user(
            username=valid_data["username"],
            password=valid_data["password"],
            email=valid_data["email"],
            first_name=valid_data["first_name"],
            last_name=valid_data["last_name"],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
        ]


class CustomObtainToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username

        return token
