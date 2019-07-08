from rest_framework import serializers
from .models import UserProfileInfo
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User



class UserprofileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileInfo
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ()

