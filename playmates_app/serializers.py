from sre_constants import SUCCESS
from rest_framework import serializers
from .models import Playmate, Note
from django.contrib.auth import get_user_model, login


User = get_user_model()
class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def save(self):
        context = self.context
        request = context.get("request")
        validated_data = self.validated_data
        email =  validated_data.get("email")
        password = validated_data.get("password")
        user = User.objects.get(email = email)
        
        if user.check_password(password):
            print("SUCCESS")
            login(request, user)
            
class PlayMateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()
    
    class Meta:
        model = Playmate
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    playmate = serializers.StringRelatedField()

    class Meta:
        model = Note
        fields = ['note', 'playmate']
class CreateUpdateNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['note', 'playmate']