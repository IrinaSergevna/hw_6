from django.contrib import admin
from django.urls import path, include
from catalog.apps import CatalogConfig
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
