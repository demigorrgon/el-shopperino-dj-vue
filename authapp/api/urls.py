# from rest_framework import routers
from django.urls import path
from authapp.api.views import (
    UserCreateViewSet,
    VerifyEmailToken,
    VerifyEmailCodeByClickingLink,
    SendMailView,
)
from rest_framework.urlpatterns import format_suffix_patterns

# base endpoint: api/v1/auth/

# router = routers.DefaultRouter()
# router.register("", UserCreateViewSet, basename="user")

# urlpatterns = router.urls
user_list = UserCreateViewSet.as_view({"get": "list", "post": "create"})
user_detail = UserCreateViewSet.as_view(
    {"get": "list", "put": "partial_update", "delete": "destroy"}
)
urlpatterns = format_suffix_patterns(
    [
        path("users/", user_list, name="user-list"),
        path("user/", user_detail, name="user-detail"),
        path("verify-email/", VerifyEmailToken.as_view(), name="verify-email"),
        path(
            "verify-email-code/<str:verification_code>/",
            VerifyEmailCodeByClickingLink.as_view(),
            name="verify-email-by-click",
        ),
        path("send-mail/", SendMailView.as_view(), name="send-mail"),
    ]
)
