import dill 

with open('similarity.est', 'rb') as f:
    similarity = dill.load(f) 

user_1 = dict(
    age=18,
    gender='male',
    location=(21.00505, 105.84566),
    rent=2e6,
)

user_2 = dict(
    age=21,
    gender='male',
    location=(20.9851472322781, 105.82419093895435),
    rent=10e6,
)

user_3 = dict(
    age=28,
    gender='fermale',
    location=(20.9851472322781, 105.82419093895435),
    rent=10e6,
)

user_4 = dict(
    age=20,
    gender='male',
    location=(21.00505, 105.84566),
    rent=2e6,
)

# compare = similarity(user_1, user_2)

example_database = [user_2, user_3, user_4]

def RecommendRoommate(user1, database):
    compare_list = []
    sorted_user_id_list = []
    for i in range(len(database)):
        compare = similarity(user1, database[i])
        compare["id"] = i+1
        compare_list.append(compare)

    sorted_user_list = sorted(compare_list, key=lambda user:user["average_sim"], reverse=True)

    for user_id in sorted_user_list:
        sorted_user_id_list.append(user_id["id"])

    return sorted_user_id_list

print(RecommendRoommate(user_1, example_database))