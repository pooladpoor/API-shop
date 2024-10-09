from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import get_object_or_404
from .models import Cart
from .serializers import CartSerializer
from rest_framework import status


class CartViews(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="جزئیات سبد خرید کاربر",
        responses=CartSerializer
    )
    def get(self, request: Request):
        user = request.user
        cart = get_object_or_404(Cart, user=user)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class CartPaidViews(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="هزینه سبد خرید پرداخت میشود",
    )
    def post(self, request: Request):
        user = request.user
        cart = get_object_or_404(Cart, user=user)
        cart.paid = True
        cart.save()
        return Response({"status": "Successfully paid"}, status=status.HTTP_200_OK)