import datetime

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(label="Дата рождения")
    location = forms.CharField(label="Город")
    address = forms.CharField(label="Адрес")
    phone_num = forms.CharField(label="Номер телефона")

    class Meta:
        model = UserProfile
        fields = ['birth_date', 'location', 'address', 'phone_num', 'profile_pic']
        widgets = {'birth_date': forms.DateInput(format='%d/%m/%Y')}
