from rest_framework import serializers
from authapp.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django_countries.serializers import CountryFieldMixin


class UserSerializer(CountryFieldMixin, serializers.ModelSerializer):
    verify_email_link = serializers.SerializerMethodField(read_only=True)

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
            "email_verified",
            "email_verification_code",
            "verify_email_link",
        ]

    def get_verify_email_link(self, obj):
        return f"/api/v1/auth/verify-email-code/{obj.email_verification_code}"


class CustomObtainToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        token["email_code"] = str(user.email_verification_code)

        return token
