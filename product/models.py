from django.db import models
from accuont.models import User


class Category(models.Model):
    title = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    
    SIZE_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]
    
    category    = models.ManyToManyField(Category, related_name="product")
    name        = models.CharField(max_length=30)
    price        = models.PositiveIntegerField(default=0)
    color       = models.CharField(max_length=20)
    size        = models.IntegerField(choices=SIZE_CHOICES)
    stock       = models.PositiveIntegerField(default=0)  # تعداد موجودی محصول

    def __str__(self):
        return f"{self.color} {self.name}"
    
    
class Coment(models.Model):
    product     = models.ForeignKey(Product, related_name="coments",on_delete=models.CASCADE)
    user        = models.ForeignKey(User, related_name="coments", on_delete=models.CASCADE)
    text        = models.TextField()