from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# from rest_framework.documentation import include_docs_urls
# from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import TokenRefreshView
from authapp.api.views import TokenObtainUsernameView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainUsernameView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("docs/", include_docs_urls(title="el-shopperinjoAPI")),
    # path(
    #     "schema",
    #     get_schema_view(
    #         title="el-shopperinjoAPI", description="api schema", version="1.0.0"
    #     ),
    #     name="coreapi_schema",
    # ),
    path("v1/api/", include("authapp.api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
