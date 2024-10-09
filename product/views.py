from drf_spectacular.utils import extend_schema
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Product, Coment, Category
from shopping_cart.models import CartItem, Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer, CategorytSerializer
from .serializer import ComentSerializer


class AddToCartView(LoginRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]

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


class ListAddToCartView(LoginRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]

    def setup(self, request, *args, **kwargs):
        self.cart , created = Cart.objects.get_or_create(user=request.user)
        super().setup(request, *args, **kwargs)
        
    def add_to_cart(self, request, product_id, number):
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=self.cart, product=product)
        cart_item.quantity += number  # تعداد محصول را افزایش می‌دهد
        cart_item.save()
    
    @extend_schema(
        summary="افزودن محصولات سبد خرید",
        description="آیدی هر محصول و تعدادش رو به فرمت زیر بفرستید",
        request={
            'application/json': {
                'example': {
                    'product_id 1': 'number 1',
                    'product_id 2': 'number 2'
                            }}},
                    )
    def post(self, request: Request):
        data: dict = request.data
        try:
            for product_id, number in data.items():
                self.add_to_cart(request, product_id, number)
        except:
            return Response(None, status.HTTP_400_BAD_REQUEST)
        return Response(None, status.HTTP_201_CREATED)


class AddComent(LoginRequiredMixin, APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=ComentSerializer,
        summary="کامنت برای محصول",
    )
    def post(self, reqest: Request, product_id):
        user = reqest.user
        product = get_object_or_404(Product, id=product_id)
        
        serilizer = ComentSerializer(data=reqest.data)
        if serilizer.is_valid():
            vla_data = serilizer.validated_data
            vla_data["user"] = user
            vla_data["product"] = product
        
            Coment.objects.create(**vla_data)
            return Response(None, status=status.HTTP_201_CREATED)
        return Response({"eror": "data is not valid"}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
        summary="لیست دسته بندی ها",
            )
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorytSerializer


# region product

@extend_schema(
        summary="لیست همه محصولات",
            )
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
@extend_schema(
        summary="لیست محصولات بر اساس دسته بندی",
            )
class CategoryProductList(APIView):
    def get(self, request:Request, category_id):
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.all().filter(category=category)
        seilizer = ProductSerializer(instance=products, many=True)
        return Response(seilizer.data, status=status.HTTP_200_OK)


@extend_schema(
        summary="جزئیات هر محصول",
            )
class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
# endregion
