from django.db import models


class Place(models.Model):
    date = models.CharField(max_length=511)
    time = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    img = models.ImageField(upload_to='map')
