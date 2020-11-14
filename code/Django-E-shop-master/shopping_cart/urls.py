from django.urls import path
from django.contrib import admin
from .views import *


admin.autodiscover()

urlpatterns = [
    path('', show_cart, name='cart'),
    path('clear', clear_cart, name='clear_cart'),
    path('del/<str:name>', delete_item, name='delete_from_cart')
]
