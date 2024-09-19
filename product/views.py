from drf_spectacular.utils import extend_schema
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Product, Coment
from shopping_cart.models import CartItem, Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer
from .serializer import ComentSerializer


class AddToCartView(LoginRequiredMixin, APIView):
    @extend_schema(
        summary="افزودن محضول به سبد خرید",
    )
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1  # تعداد محصول را افزایش می‌دهد
        cart_item.save()
        return Response(None, status.HTTP_201_CREATED)


class AddComent(LoginRequiredMixin, APIView):
    @extend_schema(
        request=ComentSerializer,
        summary="کامنت برای محصول",
    )
    def post(self, reqest: Request, product_id):
        user = reqest.user
        if not user.is_authenticated:
            return Response({"eror": "Anonymous User"}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, id=product_id)
        
        serilizer = ComentSerializer(data=reqest.data)
        if serilizer.is_valid():
            vla_data = serilizer.validated_data
            vla_data["user"] = user
            vla_data["product"] = product
        
            Coment.objects.create(**vla_data)
            return Response(None, status=status.HTTP_201_CREATED)
        return Response({"eror": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST)


# region product

@extend_schema(
        summary="لیست محصولات",
            )
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@extend_schema(
        summary="جزئیات هر محصول",
            )
class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
# endregion
