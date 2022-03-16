from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('playmates-api/', include('djoser.urls')),
    path('playmates-api/', include('djoser.urls.authtoken')),
    path('playmates-api/', include('playmates_app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
