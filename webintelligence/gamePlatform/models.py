from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)  # для url
    html_path = models.CharField(max_length=255)  # путь к HTML-файлу
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания 

    def __str__(self):
        return self.title