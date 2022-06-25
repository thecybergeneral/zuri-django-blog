from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=100)
    Text = models.TextField(max_length=1000000)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_Date = models.DateTimeField(default=datetime.now, blank=True)
    Published_Date = models.DateTimeField(default=datetime.now, blank=True)
