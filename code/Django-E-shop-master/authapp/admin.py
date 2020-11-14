from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from authapp.models import UserProfile

admin.site.register(UserProfile)
