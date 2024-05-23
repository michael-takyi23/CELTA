from django.contrib import admin
from .models import Category, Product, Address, Order, Shipment

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(Shipment)