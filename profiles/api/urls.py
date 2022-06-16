from rest_framework import routers
from profiles.api.views import ProfileViewSet

router = routers.DefaultRouter()
router.register("", ProfileViewSet, basename="profile")
urlpatterns = router.urls
