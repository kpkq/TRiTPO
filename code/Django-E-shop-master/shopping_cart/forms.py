from django import forms

from shopping_cart.models import Order

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    location = forms.CharField(max_length=140, label="Город")
    address = forms.CharField(max_length=140, label="Адрес")
    phone_number = forms.CharField(max_length=13, label="Номер телефона")
    delivery_datetime = forms.DateField(label="Дата доставки")
    do_not_disturb = forms.BooleanField(label="Не звонить на телефон")

    class Meta:
        model = Order
        fields = ['location', 'address', 'phone_number', 'do_not_disturb', 'delivery_datetime']

