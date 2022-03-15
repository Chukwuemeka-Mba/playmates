from django import views
from django.shortcuts import render
from rest_framework import viewsets

from playmates_app.permissions import IsAuthor
from .serializers import PlayMateSerializer
from .models import Playmate
from rest_framework.permissions import IsAuthenticated
# from .permissions import IsAuthor
# Create your views here.

class PlayMates(viewsets.ModelViewSet):
    serializer_class = PlayMateSerializer
    queryset = Playmate.objects.all().order_by('-created_at')
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)