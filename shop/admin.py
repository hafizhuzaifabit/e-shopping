from django.contrib import admin
from .models import Product, CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'created_at']
    list_filter = ['stock', 'created_at']
    search_fields = ['name', 'description']
    fields = ['name', 'description', 'price', 'stock', 'image', 'image_url']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'product__name']

