from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ProductForm
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return HttpResponse('celta')

def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    order, created = Order.objects.get_or_create(buyer=request.user.buyer, product=product, defaults={'quantity': 1})
    if not created:
        order.quantity += 1
        order.save()
    messages.success(request, f'{product.name} added to your cart.')
    return redirect('product_list')


@login_required
def view_cart(request):
    orders = Order.objects.filter(buyer=request.user.buyer)
    total_quantity = sum(order.quantity for order in orders)
    total_price = sum(order.product.price.amount * order.quantity for order in orders)
    return render(request, 'cart.html',
                  {'orders': orders, 'total_quantity': total_quantity, 'total_price': total_price})


@login_required
def checkout(request):
    orders = Order.objects.filter(buyer=request.user.buyer)
    total_price = sum(order.product.price.amount * order.quantity for order in orders)
    # Implement checkout logic here, such as creating a payment record, updating inventory, etc.
    messages.success(request, f'Checkout successful. Total amount paid: {total_price}')
    orders.delete()  # Clear the cart after checkout
    return redirect('product_list')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
