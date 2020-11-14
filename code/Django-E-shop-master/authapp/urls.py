from django.urls import path
from django.contrib import admin
from .views import *

admin.autodiscover()

urlpatterns = [
    path('signup', register, name='register'),
    path('profile', profile, name='profile')
]
