from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "updated", "total_price"]
    readonly_fields = ("items",)
    list_filter = ["paid", 'updated']


@admin.register(CartItem)
class CartTtemAdmin(admin.ModelAdmin):
    list_display = ["cart", "product", "quantity", "total_price"]
