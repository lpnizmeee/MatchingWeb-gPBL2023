from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class UserInfor(models.Model):
    name = models.CharField(max_length=30,blank=False)
    #email= models.CharField(max_length=50,default="")
    #locate=models.CharField(max_length=20,blank=True,null=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.BooleanField(default=True)                          # False : Girl , True : Boy
    rent = models.IntegerField(null=True,blank=True)  
    phoneNumber = models.CharField(max_length=13,null=True)
    longtitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    status = models.IntegerField(blank=True,null=True)
    password = models.CharField(max_length=30,blank=False,null=False)
    username = models.CharField(max_length=30,blank=False,null=False,unique=True)

    def __str__(self): 
        return self.name
    
# class UserMatchingInfo(models.Model):
#     class Meta:
#         model = UserInfor
#         fields = ['age','gender','longtitude','latitude','rent']

class Match(models.Model):
    userIDA = models.ForeignKey(UserInfor,related_name='matches_as_userIDA',on_delete=models.CASCADE,blank=False,null=False)
    userIDB = models.ForeignKey(UserInfor,related_name='matches_as_userIDB',on_delete=models.CASCADE,blank=False,null=False)
    status = models.IntegerField(default=0,blank=False)                        #0:保留, 1:OK, 2:キャンセル

class RentalHouse(models.Model):
    address = models.CharField(max_length=100,null=False,blank=False)
    rent = models.FloatField(blank=False)
    numberOfTenants = models.IntegerField(default=5,blank=True)
    status = models.BooleanField(default=True)  # False : full , True: empty

class Message(models.Model):
    # userIDA = models.ForeignKey(UserInfor,on_delete=models.CASCADE,blank=False,null=False)
    # userIDB = models.ForeignKey(UserInfor,on_delete=models.CASCADE,blank=False,null=False)
    message = models.CharField(max_length=100,null=True,blank=True)
    matchID = models.ForeignKey(Match,on_delete=models.CASCADE,null=False,blank=False)
    time = models.DateTimeField(auto_now_add=True)








