from django.shortcuts import render
from django.contrib.gis.db.models.functions import Distance
from .models import Shop, Delivery, Buyer
from django.contrib.gis.geos import Point
from .forms import BuyerForm

longitude = 75.576073186409
latitude = 21.010126703241255


def home(request):
    shop_location = Point(longitude, latitude, srid=4326)

    shop = Shop.objects.all()
    buyer = Buyer.objects.all()

    delivery = Delivery.objects.annotate(
        distance=Distance("location", shop_location)
    ).order_by("distance")[0:6]
    context = {
        'shops': shop,
        'delivery': delivery,
        'buyer': buyer,

    }
    return render(request, 'shops/index.html', context)


def home2(request, buyer, shop):
    shop_location = Point(shop.location.x, shop.location.y, srid=4326)

    delivery = Delivery.objects.annotate(
        distance=Distance("location", shop_location)
    ).order_by("distance")[0:6]
    context = {
        'shop': shop,
        'delivery': delivery,
        'buyer': buyer,
        'buyer_name': buyer.user,
    }
    return render(request, 'shops/index2.html', context)


def test_data(request):
    if request.POST:
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            buyer = form.cleaned_data['buyer']
            shop = form.cleaned_data['shop']
            return home2(request, buyer, shop)
    else:
        form = BuyerForm

    context = {
        'form': form,
    }
    return render(request, 'shops/form.html', context)

