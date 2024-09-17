from django.db import models

from product.models import Product
from accuont.models import User

class Cart(models.Model):
    user        = models.OneToOneField(User,related_name="ShoppingCart", on_delete=models.CASCADE)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"cart of {self.user.full_name}"
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.cart_items.all())
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        """محاسبه قیمت کل این آیتم (تعداد محصول * قیمت واحد)"""
        return self.quantity * self.product.price