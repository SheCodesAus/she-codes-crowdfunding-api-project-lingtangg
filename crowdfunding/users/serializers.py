from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
  id = serializers.ReadOnlyField()
  username = serializers.CharField(max_length=200)
  email = serializers.CharField(max_length=200)
  first_name = serializers.CharField(max_length=100)
  last_name = serializers.CharField(max_length=100)
  bio = serializers.CharField(max_length=None)
  
  def create(self, validated_data):
    return CustomUser.objects.create(**validated_data)
