# from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from django.contrib.gis.geos import Point
from osgeo import gdal

# hardcoded user location
# get user's location from IP:
# https://docs.djangoproject.com/en/1.11/ref/contrib/gis/geoip/
# or get user's location from HTML:
# https://www.w3schools.com/html/html5_geolocation.asp
latitude = 75.55928707122804
longitude = 21.00295182472697

user_location = Point(longitude, latitude, srid=4326)


# Create your views here.
class Home(generic.ListView):
    model = Shop
    context_object_name = "shops"
    queryset = Shop.objects.annotate(
        distance=Distance("location", user_location)
    ).order_by("distance")[0:6]
    template_name = "shops/index.html"
    # print(gdal.GetConfigOption('CHECK_WITH_INVERT_PROJ'))
    # print(Point(2500000, 8500000, 0.0, srid=25832).transform('EPSG:4326', clone=True))
# # @property
# def distance(self):
#     return Distance(m=distance(self.user_a.profile.location, self.user_b.profile.location).meters)
