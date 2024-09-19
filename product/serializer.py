from rest_framework import serializers
from .models import Coment


class ComentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coment
        fields = ["text"]
        