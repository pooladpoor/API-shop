from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "is_active", "last_login", "is_admin", "id", "image"]
        # TODO: image del