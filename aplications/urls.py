from django.urls import path 
from .views import *

urlpatterns = [
    path("",post_list_view,name="posts-list"),
    path("create/",create_list_view,name="create_expense"),
    path("edit/<int:pk>",edit_list_view,name="edit-lists"),
    path("delete/<int:pk>",delete_list_view,name="delete_lists"),
    
]







