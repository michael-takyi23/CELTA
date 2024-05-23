from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('gallery', gallery, name='gallery'),
    path('products', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('checkout/', checkout, name='checkout'),
    path('add_product/', add_product, name='add_product'),
]
