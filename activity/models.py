from django.db import models
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()