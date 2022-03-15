
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playmates-api/', include('djoser.urls')),
    path('playmates-api/', include('djoser.urls.authtoken')),
    path('playmates-api/', include('playmates_app.urls'))
]
