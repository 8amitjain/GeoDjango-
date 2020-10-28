from django.contrib import admin

from .models import Position, Gender, Person, FMW, SalesDeed, SalesDeedRepresentative, GiftDeed, GiftDonorDeed,\
                    PurchaseDeed, Deed

admin.site.register(Position)
admin.site.register(Gender)
admin.site.register(Person)
admin.site.register(FMW)
admin.site.register(SalesDeed)
admin.site.register(SalesDeedRepresentative)
admin.site.register(GiftDeed)
admin.site.register(GiftDonorDeed)
admin.site.register(Deed)
admin.site.register(PurchaseDeed)
