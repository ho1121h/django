from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.blog_list, name='blog_list'),#url , 함수이름(뷰에 있음), 이름
    path('list/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('write', views.blog_post, name = 'blog_post'),
    path('list/<int:blog_id>/comment', views.comment_post,name='comment_post'),
    path('like', views.user_like_post, name='like_post')
]