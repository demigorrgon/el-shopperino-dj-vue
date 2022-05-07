from rest_framework import routers
from shop.api.views import ProductViewSet


router = routers.DefaultRouter()
router.register("", ProductViewSet, basename="shop")
urlpatterns = router.urls
