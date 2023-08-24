from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from matching.models import UserInfor
from matching.serializer import UserSerializer
class UserList(APIView):
    def get(self,request):
        UserInfors = UserInfor.objects.all()
        serializer = UserSerializer(UserInfors,many=True)
        return Response(serializer.data)
    # def post(self,request):
    #     return Response({
    #         "hello": "friend"
    #     })

class UserCreate(APIView):
    def post(self,request):
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       else:
           return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
       
class UserDetail(APIView):
    def get_user_by_pk(self,pk):
        try: 
            return UserInfor.objects.get(pk=pk)
            
        except:
            return Response({
                "error": "User does not exist"
            },status = status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        try: 
            userInfor = UserInfor.objects.get(pk=pk)
            serializer = UserSerializer(userInfor)
            return Response(serializer.data)
        except:
            return Response({
                "error": "User does not exist"
            },status = status.HTTP_404_NOT_FOUND)
                
    def put(self,request,pk):                 #update
        userInfor = self.get_user_by_pk(pk)
        serializer = UserSerializer(userInfor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        userInfor = self.get_user_by_pk(pk)
        userInfor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
