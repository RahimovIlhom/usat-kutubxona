from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="USAT kutubxona",
        default_version='v1',
        description="USAT kutubxona backend",
        terms_of_service="",
        contact=openapi.Contact(email="ilhomjonrahimov217@gmail.com"),
        license=openapi.License(name="USAT library"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('', include('home.urls')),
    path('api/v1/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('library.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
