from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["product", "quantity", "total_price"]


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = ["total_price", "cart_items", "created", "updated", "paid"]
        
        

        