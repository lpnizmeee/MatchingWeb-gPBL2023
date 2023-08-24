
from django.contrib import admin
from django.urls import path
# from book_api.views import books_list,book_create 
from matching.views import UserCreate
from matching.views import UserList ,UserDetail
# from book_api.views import book
urlpatterns = [
    # path('',book_create),
    # path('list/', books_list),
    path('list/', UserList.as_view()),
    path('', UserCreate.as_view()),
    path('<int:pk>',UserDetail.as_view())
    # path('<int:pk>',book)
    
]
