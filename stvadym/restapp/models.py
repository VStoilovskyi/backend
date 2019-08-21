from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    summary = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)