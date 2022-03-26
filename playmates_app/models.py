from django.db import models
from django.conf import settings
# from django.contrib.auth.models import AbstractUser
# Create your models here.



# class User(AbstractUser):
#     pass

class Playmate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    description = models.TextField(default="Hiking, dinner date?")
    play_count = models.IntegerField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    rating = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE,
                                related_name='playmates'
                                )
    def __str__(self):
        return self.name
    
    def get_image(self):
        if self.image:
            return self.image.url
        return ''

class Note(models.Model):
    date = models.DateField(auto_now_add=True)
    note = models.TextField(default="Write a note here")
    playmate = models.ForeignKey(Playmate, related_name="notes", on_delete=models.CASCADE)

    def __str__(self):
        return self.note
