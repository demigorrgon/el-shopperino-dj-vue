from rest_framework import viewsets

# from rest_framework import permissions
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    # permission_classes = permissions.AllowAny
    # queryset = Profile.objects.filter(user__is_active=True)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = None
