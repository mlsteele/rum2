from django.db import models
from django.conf import settings

MUSIC_ROOT = settings.MUSIC_ROOT

class Song(models.Model):
    name       = models.CharField(max_length=255)
    artist     = models.CharField(max_length=255)
    album      = models.CharField(max_length=255)
    path       = models.CharField(max_length=255, unique=True) # path relative to MUSIC_ROOT to song file
    format     = models.CharField(max_length=255)

    autoloaded = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.path
