from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Gallery(models.Model):
    title = models.CharField(max_length=20)
    image = models.FileField(upload_to='mediafiles')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add='true')

class UpcomingEvent(models.Model):
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

class BlogPost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,auto_created=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True,null=True)