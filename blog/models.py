from importlib.resources import contents
from venv import create
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
#RDB 관리를 파이썬 내에서 application내에서 하자

# Create your models here.


class UserLikePost(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    create_at = models.DateTimeField("작성일자",auto_now_add=True)
    updated_at = models.DateTimeField("수정일자", auto_now=True)

class Post(models.Model):
    title = models.CharField('제목',max_length=255)
    content = models.TextField("내용") #Text 필드
    created_at = models.DateTimeField("작성일",auto_now_add=True)
    updated_at = models.DateTimeField("수정일자", auto_now=True)

    user = models.ManyToManyField(get_user_model(), related_name='like_post', through=UserLikePost)

    def __str__(self):
        return self.title #이렇게하면 제목이 게시글에 표시된다.
        

    @property
    def get_description(self):
        return self.content[:100]

    @property
    def title_desc(self):
        return self.title + '-' + self.get_description

# 댓글 기능 구현

class Comment(models.Model):
    content = models.CharField('댓글', max_length=255)
    created_at = models.DateTimeField("작성일",auto_now_add=True)
    updated_at = models.DateTimeField("수정일자", auto_now=True)
    # comment 와 post 의 관계
    # 1:n 에서 fk 는 n 쪽에 있음( 외래 키)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')


