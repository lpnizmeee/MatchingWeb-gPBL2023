from rest_framework import serializers
from matching.models import UserInfor
from matching.models import Match
from dataclasses import field

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfor
        fields = ['name','gender','phoneNumber','age','rent','longtitude','latitude','username','password']
        

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfor
        fields = ['name','username','phoneNumber','password']

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfor
        fields = ['name','gender','phoneNumber','age','rent','longtitude','latitude']

class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfor
        fields = ['name','gender','phoneNumber','age','rent','longtitude','latitude','status','username']

class CustomerWithStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['status']
class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__" 