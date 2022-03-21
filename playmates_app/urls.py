from .views import PlayMates, Notes
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('playmates', PlayMates, basename='playmates')
router.register('notes', Notes, basename='notes')



urlpatterns = [
    path('', include(router.urls)),
]
