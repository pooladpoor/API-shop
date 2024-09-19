from django.urls import path
from .views import *

app_name = 'shopping_cart'

urlpatterns = [
    path('cart/', CartViews.as_view(), name="cart"),
    path('paid/', CartPaidViews.as_view(), name="paid"),
]