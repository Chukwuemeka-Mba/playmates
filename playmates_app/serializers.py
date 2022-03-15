from rest_framework import serializers
from .models import Playmate


class PlayMateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()
    
    class Meta:
        model = Playmate
        fields = '__all__'