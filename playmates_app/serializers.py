from rest_framework import serializers
from .models import Playmate, Note


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