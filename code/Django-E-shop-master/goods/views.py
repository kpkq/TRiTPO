from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuantityForm

from goods.models import *
from shopping_cart.models import ShoppingCart


def go_home(request):
    return redirect('/home')


def show_main(request):
    product_title = request.GET.get('search_by_name')
    if product_title is None:
        prod_list = Product.objects.all()
    else:
        prod_list = Product.objects.filter(prod_name__contains=product_title)
    return render(request, 'goods_template.html', context={'prods': prod_list})


def specific_prod(request, slug):
    product = Product.objects.get(slug__iexact=slug)
    if request.method == 'POST':
        form = QuantityForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')
            if quantity >= 0:
                product = get_object_or_404(Product, slug__iexact=slug)
                cart = ShoppingCart(request)
                cart.add(product=product,
                         quantity=quantity,
                         update_quantity=False)
    else:
        form = QuantityForm()
    return render(request, 'specitem.html', context={'prod': product, 'form': form})


def specific_vendor_prods(request, vendor_name):
    prod_list = Product.objects.filter(vendor__vendor_name__exact=vendor_name)
    return render(request, 'goods_template.html', context={'prods': prod_list})


def add_to_cart(request, slug):
    cart = ShoppingCart(request)
    product = get_object_or_404(Product, slug__iexact=slug)
    cart.add(product=product,
             quantity=1,
             update_quantity=False)
    return redirect('home')
