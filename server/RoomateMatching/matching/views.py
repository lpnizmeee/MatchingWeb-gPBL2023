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
from matching.serializer import UserSerializer,MatchSerializer
from matching.serializer import CustomerWithStatusSerializer
from matching.serializer import UpdateSerializer,RecommendSerializer
from django.db.models import Q
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
        username = request.data.get("username")
        user1 = UserInfors.objects.get(username=username)
        UserInfors = UserInfor.objects.exclude(pk=user1.pk)
        # user = request.user
        # if user == "AnonymousUser":
        #     return Response(serializer.errors,status=status.HTTP_401_BAD_REQUEST)
        ordered_objects =[]
        for user in UserInfors:
            obj = UserInfor.objects.get(pk=user.pk)
            try:
                search = Match.objects.get(userIDA=obj.pk,userIDB= user1.pk) # A <-- B: other -->user
                if search.status ==0: 
                    ordered_objects.append(obj)
            except Match.DoesNotExist:
                pass

        serializer =RecommendSerializer(ordered_objects,many=True)
        return Response(serializer.data) 
        
class UserMatch(APIView):
    def put(self,request):                 #update
        #user = request.user
        usernameA = request.data.get("usernameA")
        usernameB = request.data.get("usernameB")
        action = request.data.get("action")
        # if user == "AnonymousUser":
        #     return Response(serializer.errors,status=status.HTTP_401_BAD_REQUEST)
        userA = UserInfor.objects.get(username=usernameA)
        userB = UserInfor.objects.get(username=usernameB)
        if action == 0:      # REJECT
            try:
                objects =Match.objects.get(userIDA= userB.pk,userIDB=userA.pk)
                objects.delete()   # cancel
                return Response({"message": "Rejected!"})
            except:
                return Response({"message": "Something goes wrong!"})
        elif action == 1:    # ACCEPT
            try:
                objects =Match.objects.get(userIDA= userB.pk,userIDB=userA.pk)
                serializer = CustomerWithStatusSerializer(objects,data={"status":1})
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Accept!"})
                else :
                    return Response({"message": "Something goes wrong!"})
            except:
                return Response({"message": "Something goes wrong!"})
        elif action == 2:    # CANCEL
            try:
                objects = Match.objects.get(userIDA= userB.pk,userIDB=userA.pk)
                objects.delete()
                return Response({"message": "Unfriend!"})
            except Match.DoesNotExist:
                # new match
                try:
                   objects = Match.objects.get(userIDA= userA.pk,userIDB=userB.pk)
                   objects.delete()
                   return Response({"message": "Unfriend!"})
                except Match.DoesNotExist: 
                    return Response({"message": "Something goes wrong!"})
        elif action ==3:    #  MATCH NOW
            try:
                objects = Match.objects.get(userIDA= userB.pk,userIDB=userA.pk)
                objects.delete()
                #return Response({"message": "Something goes wrong!"})
            except Match.DoesNotExist:
                pass
            data = {
                    "userIDA" : userA.pk,
                    "userIDB" : userB.pk,
                    "status" : 0
                }
            serializer = MatchSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Successfully send request to match"})
            else :
                return Response({"message": "Fail to send request"})
            # newMatch = Match.objects.create_user(userIDA=userA.pk, userIDB = userB.pk,status =0)
            # newMatch.save()
                #return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif action==4:    # WAITING
            try:
                objects = Match.objects.get(userIDA= userA.pk,userIDB=userB.pk)
                return Response({"message": "Waiting!"})
            except Match.DoesNotExist:
                return Response({"message": "Something goes wrong"})
        elif action==5:    # Cancel for A->B
            try:
                objects = Match.objects.get(userIDA= userA.pk,userIDB=userB.pk)
                objects.delete()
                return Response({"message": "Cancel!"})
            except Match.DoesNotExist:
                return Response({"message": "Something goes wrong"})
        else :
            return Response({"message": "Something goes wrong"})
##############################            
class UserSearch(APIView):
    def post(self,request):
        username = request.data.get("username")
        keyword = request.data.get("keyword")
        words = keyword.split(" ")
        user1 = UserInfor.objects.get(username=username)
        if keyword=="male":
            keyword =True
        if keyword=="female":
            keyword=False
        user = UserInfor.objects.all()
        for word in words:
            user = user.filter(
                Q(name__icontains=word) |
                Q(age__icontains=word) |
                Q(gender__icontains=word)|
                Q(phoneNumber__icontains=word) |
                Q(rent__icontains=word) 
                #Q(longtitude__icontains=keyword)
                )
            
        ordered_objects = []
        for obj in user:
            #obj = UserInfor.objects.get(pk=pk)
            #serializer =UserSerializer(obj)
            try:
                search = Match.objects.get(userIDB=obj.pk,userIDA= user1.pk) # A -> B : user -> other
                if search.status == 1 :     # match
                    obj.status = 1
                elif  search.status == 0 :  # 1 side
                    obj.status = 3          # waiting
                else: 
                    obj.status =2           # cancel --> nothing
            except Match.DoesNotExist:
                try:
                    search = Match.objects.get(userIDA=obj.pk,userIDB= user1.pk) # A <-- B: other -->user
                    if search.status ==0: 
                        obj.status = 0
                    elif search.status ==1: 
                        obj.status = 1      # accept
                    else: 
                        obj.status =2 # match
                except:
                    obj.status = 2    # NOTHING
            #serializer1 = RecommendSerializer(status)
            
            ordered_objects.append(obj)
        
        serializer = RecommendSerializer(ordered_objects,many=True)
        #return Response({'access_token': access_token})
        return Response(serializer.data)
###################
class UserChat(APIView):
    def post(self,request):
        usernameA = request.data.get("usernameA")
        usernameB = request.data.get("usernameB")
        userA = UserInfor.objects.get(username=usernameA)
        userB = UserInfor.objects.get(username=usernameB)
        try:
            objects = Match.objects.get(userIDA= userA.pk,userIDB=userB.pk)
            serializer = MatchSerializer(objects)
            return Response(serializer.data)
        except Match.DoesNotExist:
            try:
                objects = Match.objects.get(userIDA= userB.pk,userIDB=userA.pk)
                serializer = MatchSerializer(objects)
                return Response(serializer.data)
            except Match.DoesNotExist:
                return Response({"message": "Something goes wrong"})       


##############################
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
           
            compare = similarity(user1_dict,user2_dict)
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
                search = Match.objects.get(userIDB=obj.pk,userIDA= user1.pk) # A -> B : user -> other
                if search.status == 1 :     # match
                    obj.status = 1
                elif  search.status == 0 :  # 1 side
                    obj.status = 3          # waiting
                else: 
                    obj.status =2           # cancel --> nothing
            except Match.DoesNotExist:
                try:
                    search = Match.objects.get(userIDA=obj.pk,userIDB= user1.pk) # A <-- B: other -->user
                    if search.status ==0: 
                        obj.status = 0
                    elif search.status ==1: 
                        obj.status = 1      # accept
                    else: 
                        obj.status =2 # match
                except:
                    obj.status = 2    # NOTHING
            #serializer1 = RecommendSerializer(status)
            
            ordered_objects.append(obj)
            
        serializer =RecommendSerializer(ordered_objects,many=True)
        return Response(serializer.data) 
        #return Response(ordered_objects)


