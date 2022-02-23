from django.urls import path
from blog.views import post_list, post_detail, post_new 

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/detail/<int:post_pk>', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
]