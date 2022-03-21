from django import views
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import NoteSerializer, PlayMateSerializer, CreateUpdateNoteSerializer
from .models import Playmate, Note


class PlayMates(viewsets.ModelViewSet):
    serializer_class = PlayMateSerializer
    queryset = Playmate.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class Notes(viewsets.ModelViewSet):
    serializer_class = CreateUpdateNoteSerializer
    queryset = Note.objects.all().order_by('-date')

    def list(self, queryset):
        queryset = self.get_queryset()
        serializer = NoteSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def retrieve(self, queryset):
        queryset = self.get_queryset()
        serializer = NoteSerializer(queryset)
        return Response(serializer.data)