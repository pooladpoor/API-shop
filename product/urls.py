from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('add_to_cart/<int:product_id>', AddToCartView.as_view(), name="add_to_cart"),
    path('add_coment/<int:product_id>', AddComent.as_view(), name="add_conent"),
    path('', ProductList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
]