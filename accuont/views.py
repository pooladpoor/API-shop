from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User
from .serializer import UserSerializer


class CustomAuthToken(ObtainAuthToken):
    @extend_schema(
        summary="ایجاد توکن برای اهراز هویت",
        description="برای هر کاربر از اینجا توکن ایجاد کنید و در هدر درخواست های بعدی ارسال شود",
    )
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(user_name=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
            })
        return Response({'error': 'The national code or password is invalid'}, status=400)


class SignUpViews(APIView):
    @extend_schema(
        summary="ثبت نام کاربر",
        request=UserSerializer,
        description="date_of_birth , adress , national_code : الزامی نیست"
    )
    def post(self, reqest: Request):
        serializer = UserSerializer(data=reqest.data)
        if serializer.is_valid():
            val_data = serializer.validated_data
            User.objects.create_user(**val_data)
            return Response({'status': 'User successfully created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'The information is invalid'}, status=status.HTTP_400_BAD_REQUEST)


class EditProfile(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="دریافت اطلاعات کاربر",
        responses=UserSerializer,
    )
    def get(self, request:Request):
        user = request.user
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
        summary="ارسال اطلاعات برای اپدیت",
        request=UserSerializer,
    )
    def put(self, request: Request):
        user = request.user
        data = request.data
        serializer = UserSerializer(instance=user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Details": "user updated"}, status=status.HTTP_200_OK)
        else:
            return Response({"Details": "data is invalid"}, status=status.HTTP_400_BAD_REQUEST)