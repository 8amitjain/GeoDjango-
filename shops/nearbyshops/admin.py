from django.contrib import admin
from .models import Shop, Buyer, Delivery
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):   # OSMGeoAdmin
    list_display = ("user", "name", "location")
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):   # OSMGeoAdmin
    list_display = ("user", "location")
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):   # OSMGeoAdmin
    list_display = ("user", "location")
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }
