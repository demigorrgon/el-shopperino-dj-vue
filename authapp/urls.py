from rest_framework import routers
from authapp.api.views import UserCreateViewSet


router = routers.DefaultRouter()
router.register("", UserCreateViewSet, basename="user")
urlpatterns = router.urls
