from django.db import models
from django.contrib.auth.models import AbstractUser
import os
import uuid

# Create your models here.

def file_upload(instance, filename):
     ext = filename.split('.')[-1]
     filename = f'{instance.username}.{ext}'
     return os.path.join('username/avatars/', filename)



class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(upload_to=file_upload, blank=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ["-date_joined"]

    def __str__(self) -> str:
        if self.full_name:
            return self.full_name
        else:
            return self.email or self.username
    
    @property
    def full_name(self):
            return f"{self.last_name} {self.first_name} {self.middle_name}"
    

    

