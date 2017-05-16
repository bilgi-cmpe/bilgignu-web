from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    pattern = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    pattern = models.CharField(max_length=100)
    redirect = models.BooleanField()
    url = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name
