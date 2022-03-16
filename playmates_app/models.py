from django.db import models
# from users.models import User
from django.conf import settings
# Create your models here.

class Playmate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    description = models.TextField(default="One night stand, gangbag, both?")
    slug = models.SlugField()
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