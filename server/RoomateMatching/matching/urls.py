
from django.contrib import admin
from django.urls import path
# from book_api.views import books_list,book_create 
from matching.views import UserCreate,UserLogin
from matching.views import UserList ,UserDetail
from matching.views import UserRecommend,UserUpdate
from matching.views import UserMatch,UserSearch
from matching.views import UserChat
# from book_api.views import book
urlpatterns = [
    # path('',book_create),
    # path('list/', books_list),
    path('list/', UserList.as_view()),
    path('', UserCreate.as_view()),
    path('<int:pk>',UserDetail.as_view()),
    path('login/',UserLogin.as_view()),
    path('recommend/',UserRecommend.as_view()) ,
    # path('<int:pk>',book)
    path('update/',UserUpdate.as_view()),
    path('match/',UserMatch.as_view()),
    path('usersearch/',UserSearch.as_view()),
    path('userchat/',UserChat.as_view()),
    
]
