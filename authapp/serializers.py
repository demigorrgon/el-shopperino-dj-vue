from rest_framework import serializers
from authapp.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django_countries.serializers import CountryFieldMixin


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        )

    def create(self, valid_data):
        user = CustomUser.objects.create_user(
            username=valid_data["username"],
            password=valid_data["password"],
            email=valid_data["email"],
            first_name=valid_data["first_name"],
            last_name=valid_data["last_name"],
            country=valid_data["country"],
        )
        return user


class UserSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "country",
        ]


class CustomObtainToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username

        return token
