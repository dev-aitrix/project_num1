from rest_framework import serializers
from .models import *

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ProductOrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = '__all__'