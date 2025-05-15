from django.db import models
from django.utils import timezone
class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)  # для url
    html_path = models.CharField(max_length=255)  # путь к HTML-файлу
    created_at = models.DateTimeField(default=timezone.now)  # Дата создания 

    def __str__(self):
        return self.title