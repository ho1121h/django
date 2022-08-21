from attr import field
from django import forms
from .models import Post

#  좀더 세련된 방법

# Form 을 파이썬에서 관리함
# 대체로 모델과 비슷하다
# 입력을 받는 것은 DB에서 넣고 받기 때문

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     content = forms.CharField(widget=forms.Textarea)

#https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
# 설정한 필드에 맞춰 알아서 만들어줌
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']
