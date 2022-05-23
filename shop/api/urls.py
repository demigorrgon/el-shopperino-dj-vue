# from rest_framework import routers
from shop.api.views import (
    ProductViewSet,
    OrderViewSet,
    UsersOrdersViewSet,
    CategoryViewSet,
)
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


# router = routers.DefaultRouter()
# router.register("", ProductViewSet, basename="shop")
# router.register("order", OrderViewSet, basename="order")
# urlpatterns = router.urls
product_list = ProductViewSet.as_view({"get": "list", "post": "create"})
product_detail = ProductViewSet.as_view(
    {
        "get": "retrieve",
        "post": "create",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
order_list = OrderViewSet.as_view({"get": "list", "post": "create"})
order_detail = OrderViewSet.as_view(
    {
        "get": "retrieve",
        "post": "create",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
users_order_list = UsersOrdersViewSet.as_view({"get": "list", "post": "create"})
users_order_detail = UsersOrdersViewSet.as_view(
    {
        "get": "retrieve",
        "post": "create",
        "patch": "partial_update",
        "delete": "destroy",
    }
)
categories_list = CategoryViewSet.as_view({"get": "list", "post": "create"})

urlpatterns = format_suffix_patterns(
    [
        path("products/", product_list, name="product-list"),
        path("product/<int:pk>/", product_detail, name="product-detail-pk"),
        path("product/<str:slug>/", product_detail, name="product-detail-slug"),
        path("orders/", order_list, name="order-list"),
        path("orders/<int:pk>/", order_detail, name="order-detail"),
        path("orders/user/<int:pk>/", users_order_list, name="users-order-list"),
        path(
            "orders/user/<int:pk>/order/<int:order_id>/",
            users_order_detail,
            name="users-order-detail",
        ),
        path("categories/", categories_list, name="category-list"),
    ]
)
