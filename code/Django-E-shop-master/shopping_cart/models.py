from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


# Create your models here.
from goods.models import Product


class ShoppingCart(models.Model):

    def __str__(self):
        return self

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price),
                                     'name': product.prod_name}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
            self.cart[product_id]['price'] = product.price * quantity
        else:
            self.cart[product_id]['quantity'] += quantity
            self.cart[product_id]['price'] = product.price * self.cart[product_id]['quantity']
        self.cart[product_id]['price'] = round(self.cart[product_id]['price'], 2)
        self.store()

    def delete_from_cart(self, product):
        del self.cart[str(product.id)]
        self.store()

    def store(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def clear(self):
        try:
            del self.session[settings.CART_SESSION_ID]
        except KeyError:
            print('cart is almost empty')

    def get_cart(self):
        try:
            cart_list = []
            for cart_item in self.session[settings.CART_SESSION_ID]:
                cart_list.append(self.session[settings.CART_SESSION_ID][cart_item])
        except KeyError:
            return []
        return cart_list

    def get_total(self):
        try:
            total = 0.0
            for cart_item in self.session[settings.CART_SESSION_ID]:
                total += self.session[settings.CART_SESSION_ID][cart_item]['price']
        except KeyError:
            return 0.0
        return total


class CartItem(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prod = Product()
        self.quantity = 0
        self.price = 0

    def create_cart_item_from_session(self, session_dict):
        self.prod = Product.objects.get(prod_name__exact=session_dict['name'])
        self.quantity = session_dict['quantity']
        self.price = session_dict['price']

    def __str__(self):
        return self.prod


class Order(models.Model):
    total = models.FloatField(default=0.0)
    location = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    prod_list = models.CharField(max_length=255, null=True)
    do_not_disturb = models.BooleanField()
    phone_num = models.CharField(max_length=14, default="+375")
    delivery_datetime = models.DateField(blank=True)
    add_date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.address
