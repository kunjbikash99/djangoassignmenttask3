from django.db import models
from django.contrib.auth.models import User
#from django.core import validators
#from django import forms
# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField()
    verify_email=models.EmailField()
    contact=models.CharField(max_length=20)
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.username

class already(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=15)

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


