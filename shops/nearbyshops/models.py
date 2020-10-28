from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.gis.measure import Distance, D
from geopy.distance import distance


class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.PointField(srid=4326)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.PointField(srid=4326)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Delivery(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.user.username


class FormNear(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

