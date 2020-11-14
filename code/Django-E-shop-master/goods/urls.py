from django.urls import path, include
from django.contrib import admin
from .views import *

admin.autodiscover()

urlpatterns = [
    path('home', show_main, name='home'),
    path('', go_home),
    path('home/<str:slug>/add', add_to_cart, name='add'),
    path('home/<str:slug>', specific_prod, name='specific_prod_url'),
    path('vendor/<str:vendor_name>', specific_vendor_prods, name='spec_vendor_url'),
]