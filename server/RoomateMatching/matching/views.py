from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.forms.models import model_to_dict
# Create your views here.
import dill 
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from matching.models import UserInfor,Match
from matching.serializer import UserSerializer,RegisterSerializer
#from matching.serializer import CustomerWithStatusSerializer
from matching.serializer import UpdateSerializer,RecommendSerializer
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

class UserUpdate(APIView):
    def put(self,request):                 #update
        user = request.user
        if user == "AnonymousUser":
            return Response(serializer.errors,status=status.HTTP_401_BAD_REQUEST)
        user1 = UserInfor.objects.get(username=user.get_username())
        serializer = UpdateSerializer(user1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserNotification(APIView):
    def get(self,request):
        user = request.user
        if user == "AnonymousUser":
            return Response(serializer.errors,status=status.HTTP_401_BAD_REQUEST)
        try: 
            userInfor = UserInfor.objects.get(username=user.get_username())
            invitations = Match.objects.filter(userIDB=userInfor.pk)
            ordered_objects=[]
            for userId in invitations:
                obj = UserInfor.objects.get(pk = userId.userIDA)
                ordered_objects.append(obj)
            serializer = UserSerializer(ordered_objects,many=True)
            return Response(serializer.data)
        except:
            return Response({
                "error": "User does not exist"
            },status = status.HTTP_404_NOT_FOUND)
        
class UserMatch(APIView):
    def post(self,request):
       serializer = RegisterSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save() 
           user = User.objects.create_user(username=serializer.data['username'], password=serializer.data['password'],email="Duong.Dt@gmail.com")
           user.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND) 
       
    def put(self,request):                 #update
        user = request.user
        usernameB = request.data.get("username")
        if user == "AnonymousUser":
            return Response(serializer.errors,status=status.HTTP_401_BAD_REQUEST)
        user1 = UserInfor.objects.get(username=user.get_username())
        user2 = UserInfor.objects.get(username=usernameB)
        data = {
            "userIDA": user1.pk,
            "userIDB": user2.pk,
            "status": 1,
            # Các trường khác tùy ý
        }
        newMatch = Match.objects.create_user(user)
        user.save()
        serializer = UpdateSerializer(user1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#########################
with open('similarity.est', 'rb') as f:
        similarity = dill.load(f)    

class UserRecommend(APIView):   
    def RecommendRoommate(self,user1, database):
        compare_list = []
        sorted_user_id_list = []
        user1_js = {
                "age": user1.age,
                "gender": user1.gender,
                "location": (user1.longtitude, user1.latitude),
                "rent": user1.rent, 
              }
        user1_json = json.dumps(user1_js)  # Chuyển từ dict thành JSON chuỗi
        user1_dict = json.loads(user1_json)  # Chuyển từ JSON chuỗi thành dict
        for user2 in database:
            user2_js = {
                "age": user2.age,
                "gender": user2.gender,
                "location": (user2.longtitude, user2.latitude),
                "rent": user2.rent, 
              }
            
            user2_json = json.dumps(user2_js)  # Chuyển từ dict thành JSON chuỗi
            user2_dict = json.loads(user2_json)  # Chuyển từ JSON chuỗi thành dict
           
            compare = similarity(user1_dict,user2_dict )
            compare["id"] = user2.id
            compare_list.append(compare)
        
        sorted_user_list = sorted(compare_list, key=lambda user:user["average_sim"], reverse=True)

        for user_id in sorted_user_list:
            sorted_user_id_list.append(user_id["id"])

        return sorted_user_id_list
    
    def post(self,request):
        #user = request.user
        user1 = UserInfor.objects.get(username=request.data.get("username"))
        #UserInfors = UserInfor.objects.all()
        UserInfors = UserInfor.objects.exclude(pk=user1.pk)
        #users_recommend_list = list(UserInfors)
        sorted_user_id_list = self.RecommendRoommate(user1,UserInfors)
        ordered_objects = []
        for pk in sorted_user_id_list:
            obj = UserInfor.objects.get(pk=pk)
            #serializer =UserSerializer(obj)
            try:
                search = Match.objects.get(userIDA=obj.pk,userIDB= user1.pk)
                obj.status = search.status
            except Match.DoesNotExist:
                obj.status = 2    # NOTHING
            #serializer1 = RecommendSerializer(status)
            
            ordered_objects.append(obj)
            
        serializer =RecommendSerializer(ordered_objects,many=True)
        #serializer2 = CustomerWithStatusSerializer(ordered_objects,many=True)
        # combined_data = {**serializer.data, **serializer2.data}
        # return Response(combined_data)
        return Response(serializer.data) 
        #return Response(ordered_objects)

