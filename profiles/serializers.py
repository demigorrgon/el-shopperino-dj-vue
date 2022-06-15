from rest_framework import serializers
from profiles.models import Profile
from django_countries.serializers import CountryFieldMixin


class ProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    country = serializers.CharField(source="user.country")

    class Meta:
        model = Profile
        fields = ("user", "created_at", "updated_at", "country")

    def get_user(self, obj):
        return obj.user.username
