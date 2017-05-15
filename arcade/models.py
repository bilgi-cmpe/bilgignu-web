from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=255)
    money = models.IntegerField(default=0)

    def __str__(self):
        return self.name
