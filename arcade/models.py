from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=255)
    money = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    start_date = models.DateField(blank=True,auto_now=False)
    end_date = models.DateField(null=True,blank=True,auto_now=False, auto_now_add=False)
    location_name = models.CharField(null=True,max_length=255)
    loc_pos_lat = models.FloatField(default=41.068178)
    loc_pos_lon = models.FloatField(default=28.946577)

    def __str__(self):
        return self.name
