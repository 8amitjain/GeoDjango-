from django.contrib.gis.db import models
from django.contrib.gis.measure import Distance, D
from geopy.distance import distance


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)


