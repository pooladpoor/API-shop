from django.contrib import admin
from .models import Product, Coment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price"]


@admin.register(Coment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product", "user"]
