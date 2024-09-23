from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('category-list/', CategoryList.as_view()),
    path('add_to_cart/', ListAddToCartView.as_view(), name="list_add_to_cart"),
    # path('add_to_cart/<int:product_id>', AddToCartView.as_view(), name="add_to_cart"),
    path('add_coment/<int:product_id>', AddComent.as_view(), name="add_conent"),
    path('', ProductList.as_view(), name="productlist"),
    path('<int:category_id>', CategoryProductList.as_view(), name="category_product_list"),
    path('<int:pk>', ProductDetail.as_view()),
]