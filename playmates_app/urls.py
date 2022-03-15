from .views import PlayMates
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PlayMates, basename='playmates')


urlpatterns = [
    path('playmates/', include(router.urls))
]
