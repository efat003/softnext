# softagency/urls.py

from django.contrib import admin
from django.urls import path
from main import views  # import your view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # root URL
    path("index/", views.index, name="index"),  # alternative index URL
    path("api/contact/", views.contact_api, name="contact_api"),  # API endpoint (disabled)
    path("api/settings/", views.update_settings, name="update_settings"),  # API endpoint (disabled)
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)