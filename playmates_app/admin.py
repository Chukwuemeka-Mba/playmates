from django.contrib import admin
from .models import Playmate, Note
# Register your models here.

@admin.register(Playmate)
class PlaymateAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'author', 'created_at', 'play_count')
    list_filter = ('created_at', 'rating', 'age', 'play_count')
    search_fields = ('name', 'description')
    ordering = ('created_at', 'play_count')

admin.site.register(Note)

