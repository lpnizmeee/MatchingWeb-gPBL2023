from rest_framework import serializers
from matching.models import UserInfor
from dataclasses import field

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfor
        fields = "__all__"
        

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfor
        fields = ['name','username','phoneNumber','password']