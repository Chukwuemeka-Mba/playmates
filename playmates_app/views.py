from logging import raiseExceptions
from urllib import response
from django import views
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import NoteSerializer, PlayMateSerializer, CreateUpdateNoteSerializer, LoginUserSerializer
from .models import Playmate, Note
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
User = get_user_model()
class LoginUserView(APIView):
    queryset = User.objects.all()
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = LoginUserSerializer
        serializer = serializer(data = request.data, context = {"request": request})
        serializer.is_valid(raise_exception = True)
        serializer.save()
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

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