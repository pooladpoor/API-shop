from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    
    # # اعتبار سنجی برای هر فیلد خواص
    # def validate_priority(self, priority):
    #     if priority < 10 or priority > 20:
    #         raise serializers.ValidationError('priority is not ok')
    #     return priority
    #
    # #  اینجا به همه فیلد ها دسرسی داری و میشه اعتبار سنجی کرد
    # # def validate(self, attrs):
    # #     print(attrs)
    # #     return super().validate(attrs)
    

    class Meta:
        model = Product
        fields = '__all__'
