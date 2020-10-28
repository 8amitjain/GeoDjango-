from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('add/', views.person_create_view, name='person_add'),
    path('add2/', views.person_create_view2, name='person_add2'),

    path('', views.select_deed, name='select-deed'),
    path('sales/', views.sales_deed, name='sales-deed'),
    path('gift/', views.gift_deed, name='gift-deed'),
    path('purchase/', views.purchase_deed, name='purchase-deed'),

    # path('deed_edit_download/', views.deed_edit_download, name='edit-download-deed'),

    path('download_form_sales/<str:unique_id>/', views.download_form_sales, name='form-download-sales'),
    path('download_form_gift/<str:unique_id>/', views.download_form_gift, name='form-download-gift'),
    path('download_form_purchase/<str:unique_id>/', views.download_form_purchase, name='form-download-purchase'),

    # Ajax
    path('ajax/load-fwn/', views.load_fwm, name='ajax-fwm-url'),  # AJAX
    path('ajax/load-fwn2/', views.load_fwm2, name='ajax-fwm-url2'),  # AJAX
    path('ajax/load-gift/', views.load_gift, name='ajax-fwm-gift'),  # AJAX
    path('ajax/load-gift2/', views.load_gift2, name='ajax-fwm-gift2'),  # AJAX

    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX
    path('ajax/load-income/', views.load_income, name='ajax_load_income'),  # AJAX
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
