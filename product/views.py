from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from shopping_cart.models import CartItem, Cart

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


class AddToCartView(LoginRequiredMixin,APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1  # تعداد محصول را افزایش می‌دهد
        cart_item.save()
        return Response(None, status.HTTP_201_CREATED)
