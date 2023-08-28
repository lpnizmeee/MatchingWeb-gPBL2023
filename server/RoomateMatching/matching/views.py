from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from matching.models import UserInfor
from matching.serializer import UserSerializer,RegisterSerializer
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
       serializer = RegisterSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           
           user = User.objects.create_user(username=serializer.data['username'], password=serializer.data['password'],email="Duong.Dt@gmail.com")
           user.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
       
class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Thực hiện xác thực người dùng
        user = authenticate(username=username, password=password)
        
        if user is not None:
            #refresh = RefreshToken.for_user(user)
            #access_token = str(refresh.access_token)
            login(request,user)
            person = UserInfor.objects.get(username=user.get_username())
            serializer = UserSerializer(person)
            #return Response({'access_token': access_token})
            return Response(serializer.data)
        else:
            return Response({'error': 'Tên đăng nhập hoặc mật khẩu không đúng.'}, status=status.HTTP_401_UNAUTHORIZED)
       
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
