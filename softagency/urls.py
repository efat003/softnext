<<<<<<< HEAD
# softagency/urls.py

from django.contrib import admin
from django.urls import path
from main import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.contrib import admin
from django.urls import path
from main import views    # import the view you just wrote

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),   # root URL
]
>>>>>>> bb3c4565876e5acdfee31cb8c71a893022933ece
