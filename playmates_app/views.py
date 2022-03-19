from argparse import Action
from django import views
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import PlayMateSerializer
from .models import Playmate


class PlayMates(viewsets.ModelViewSet):
    serializer_class = PlayMateSerializer
    queryset = Playmate.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)
