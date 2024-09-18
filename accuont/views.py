from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .models import User


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        national_code = request.data.get('national_code')
        password = request.data.get('password')
        user = authenticate(national_code=national_code, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
            })
        return Response({'error': 'The national code or password is invalid'}, status=400)


class SignUpViews(APIView):
    def post(self, reqest: Request):
        data = reqest.data
        try:
            User.objects.create_user(
            full_name       =data.get("full_name"),
            phone           =data.get("phone"),
            national_code   =data.get("national_code"),
            password        =data.get("password"),
            date_of_birth   =None,
            adress          =None,
            )
            return Response(None, status=status.HTTP_201_CREATED)
        
        except KeyError:
            return Response({'error': 'The information is invalid'}, status=status.HTTP_400_BAD_REQUEST)
