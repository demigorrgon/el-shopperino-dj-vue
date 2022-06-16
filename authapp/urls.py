from rest_framework import routers
from authapp.api.views import UserCreateViewSet


router = routers.DefaultRouter()
router.register("auth", UserCreateViewSet, basename="user")
urlpatterns = router.urls
