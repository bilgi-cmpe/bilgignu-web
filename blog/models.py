from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    pattern = models.CharField(max_length=100)

    def __str__(self):
        return self.title
