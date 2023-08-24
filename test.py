import dill 

with open('similarity.est', 'rb') as f:
    similarity = dill.load(f) 
    
    
    
user_1 = dict(
    age=18,
    gender='male',
    location=(21.00505, 105.84566),
    rent=2e6
)


user_2 = dict(
    age=21,
    gender='male',
    location=(20.9851472322781, 105.82419093895435),
    rent=10e6
)


print(similarity(user_1, user_2))        