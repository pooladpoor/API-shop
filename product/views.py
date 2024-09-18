from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Product, Coment
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


class AddComent(LoginRequiredMixin,APIView):
    def post(self, reqest: Request, product_id):
        
        data = reqest.data
        try:
            text = data["text"]
        except:
            return Response({"error": "data in invalid"},status=status.HTTP_400_BAD_REQUEST)
        
        user = reqest.user
        if not user.is_authenticated:
            return Response({"eror": "Anonymous User"}, status=status.HTTP_400_BAD_REQUEST)
        
        product = get_object_or_404(Product, id=product_id)
        
        Coment.objects.create(product=product, user=user,text=text)
        return Response(None, status=status.HTTP_201_CREATED)
    