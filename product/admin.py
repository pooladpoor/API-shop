from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","price"]


@admin.register(Coment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product", "user"]
    
    
@admin.register(Category)
class CatgoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
