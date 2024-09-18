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











#  جواب نداد چون هر ریکوست جدا برسی میشه و تو درخواست بعدی دیگه لاگین نیست
# class login(APIView):
#     def post(self, request:Request):
#         data = request.data
#         print("data: ", data)
#         print("user: ",request.user)
#
#         try:
#             nc = data["national_code"]
#             p = data["password"]
#         except:
#             return Response({"national_code":"...", "password":"..."}, status=status.HTTP_400_BAD_REQUEST)
#
#         user = authenticate(request, national_code=nc, password=p)
#         print("user: ", user)
#         if user is not None:
#             login(request=request,user=user)
#             return Response(None, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(None, status=status.HTTP_406_NOT_ACCEPTABLE)
