from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deed/', include('deed.urls')),
    path('', include('nearbyshops.urls')),

]
