from django.conf import settings

# Create your views here.
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404

from authapp.forms import UserUpdateForm, ProfileUpdateForm
from goods.models import Product
from shopping_cart.forms import OrderForm
from shopping_cart.models import ShoppingCart, CartItem, Order


@login_required
def show_cart(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cart_list = ShoppingCart(request).get_cart()
            cart_item_list = ""
            for cart in cart_list:
                item = CartItem()
                item.create_cart_item_from_session(cart)
                cart_item_list += "id: " + str(item.prod.id) + " " + item.prod.prod_name +\
                                  " Количество: " + str(item.quantity) + ", "
            order = Order()
            order.address = form.cleaned_data["address"]
            order.location = form.cleaned_data["location"]
            order.phone_number = form.cleaned_data["phone_number"]
            order.total = ShoppingCart(request).get_total()
            order.delivery_datetime = form.cleaned_data["delivery_datetime"]
            order.do_not_disturb = form.cleaned_data["do_not_disturb"]
            order.prod_list = cart_item_list
            order.save()
        return redirect('cart')
    else:
        form = OrderForm(initial={'address': request.user.userprofile.address,
                                  'location': request.user.userprofile.location,
                                  'phone_number': request.user.userprofile.phone_num,
                                  'total': ShoppingCart(request).get_total()})

        cart_list = ShoppingCart(request).get_cart()
        cart_item_list = []
        for cart in cart_list:
            item = CartItem()
            item.create_cart_item_from_session(cart)
            cart_item_list.append(item)
    return render(request, 'cart.html', context={'cart': cart_item_list, 'total': ShoppingCart(request).get_total(),
                                                 'form': form})


def clear_cart(request):
    ShoppingCart(request).clear()
    return redirect('cart')


def delete_item(request, name):
    product = get_object_or_404(Product, prod_name__iexact=name)
    print(product)
    cart = ShoppingCart(request)
    cart.delete_from_cart(product)
    cart_list = ShoppingCart(request).get_cart()
    print(ShoppingCart(request).get_total())
    return redirect('cart')
