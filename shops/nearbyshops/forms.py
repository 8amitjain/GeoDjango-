from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget
from django import forms

from .models import FormNear


# class CityForm(forms.ModelForm):
#     class Meta:
#         model = City
#         fields = ("name", "location")
#         widgets = {
#             'location': GooglePointFieldWidget,
#             # 'name': GoogleStaticOverlayMapWidget,
#         }


class BuyerForm(forms.ModelForm):
    class Meta:
        model = FormNear
        fields = ("buyer", "shop")
