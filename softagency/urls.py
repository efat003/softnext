from django.contrib import admin
from django.urls import path
from main import views    # import the view you just wrote

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),   # root URL
]
