from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "topic" 
        verbose_name = "Topic"
        verbose_name_plural = "Topics"
        ordering = ["name"] 

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='articles/thumbnails/')
    status = models.CharField(max_length=20, default='pending')
    topics = models.ManyToManyField('Topic')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'article'  
        verbose_name = "Article"  
        verbose_name_plural = "Articles"
        ordering = ["-created_at"]  

    def __str__(self):
        return self.title
