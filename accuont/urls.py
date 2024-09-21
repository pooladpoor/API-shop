from django.urls import path
from .views import *


app_name = 'accuont'

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('singup/', SignUpViews.as_view()),
    path('edit-profile/', EditProfile.as_view()),
]