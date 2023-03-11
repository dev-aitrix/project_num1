from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserManager
        fields = '__all__'
