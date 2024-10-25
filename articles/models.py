from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='articles/thumbnails/')
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('publish', 'Publish')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title
