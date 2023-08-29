import dill,json 

with open('similarity.est', 'rb') as f:
    similarity = dill.load(f) 

user_1 = dict(
    age=18,
    gender=True,
    #location=(21.00505, 105.84566),
    longtitude=21.00505,
    latitude = 105.84566,
    rent=2e6,
)

user_2 = dict(
    age=18,
    gender=True,
    #location=(20.9851472322781, 105.82419093895435),
    longtitude=20.9851472322781,
    latitude = 105.82419093895435,
    rent=10e6,
)

user_3 = dict(
    age=28,
    gender=False,
    #location=(20.9851472322781, 105.82419093895435),
    longtitude=20.9851472322781,
    latitude = 105.82419093895435,
    rent=10e6,
    
)

user_4 = dict(
    age=14,
    gender=True,
    #location= None,
    #location=(21.00505, 105.84566),
    longtitude=21.00505,
    latitude = 105.84566,
    rent=2e6
)

# compare = similarity(user_1, user_2)

example_database = [user_2, user_3, user_4]

# def RecommendRoommate(user1, database):
#     compare_list = []
#     sorted_user_id_list = []
#     for i in range(len(database)):
#         compare = similarity(user1, database[i])
#         compare["id"] = i+1
#         compare_list.append(compare)

#     sorted_user_list = sorted(compare_list, key=lambda user:user["average_sim"], reverse=True)

#     for user_id in sorted_user_list:
#         sorted_user_id_list.append(user_id["id"])

#     return sorted_user_id_list



def RecommendRoommate(user1, database):
        compare_list = []
        sorted_user_id_list = []
        user1_js = {
                "age": user1["age"],
                "gender": user1["gender"],
                "location": (user1["longtitude"], user1["latitude"]),
                "rent": user1["rent"], 
              }
        user1_json = json.dumps(user1_js)  # Chuyển từ dict thành JSON chuỗi
        user1_dict = json.loads(user1_json)  # Chuyển từ JSON chuỗi thành dict
        i=0
        for user2 in database:
            user2_js = {
                "age": user2["age"],
                "gender": user2["gender"],
                "location": (user2["longtitude"], user2["latitude"]),
                "rent": user2["rent"], 
              }
            
            user2_json = json.dumps(user2_js)  # Chuyển từ dict thành JSON chuỗi
            user2_dict = json.loads(user2_json)  # Chuyển từ JSON chuỗi thành dict
           
            compare = similarity(user1_dict,user2_dict )
            compare["id"] = i+1
            i = i+1
            compare_list.append(compare)
        
        sorted_user_list = sorted(compare_list, key=lambda user:user["average_sim"], reverse=True)

        for user_id in sorted_user_list:
            sorted_user_id_list.append(user_id["id"])

        return sorted_user_id_list

print(RecommendRoommate(user_1, example_database))
# from matching.models import UserInfor

# # List các primary key đã có
# primary_keys = [1, 2, 5, 8]

# Truy vấn và lấy danh sách các đối tượng dựa trên primary keys
# def ariticle():
#     articles = UserInfor.objects.get(pk__in=primary_keys)
#     return articles
# # In ra danh sách các đối tượng
# articles = ariticle()

# for article in articles:
#     print(article.title)

