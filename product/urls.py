from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('add_to_cart/<int:product_id>', AddToCartView.as_view(), name="add_to_cart"),
]