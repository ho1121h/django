import profile
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import is_valid_path
from sympy import content
from django.contrib.auth import get_user_model


from .models import Post ,Comment ,UserLikePost
# Create your views here.
from .forms import PostForm

profile_list =[{
    'id':1,
    'name':'홍진우',
    'height':172
},{
    'id':2,
    'name':'김유신',
    'height':180
},
]


def index(request):

    
    return render(request,'index.html',{'name':'홍진우','profile':profile_list})

#블로그 컨트롤
def blog_list(request):
    # Django-ORM은 DB를 조회할때 매니저 객체를 사용
    # Model 에서 Manager객체에 접근 -> 모델 오브젝트 / <Model>.objects
    #https://docs.djangoproject.com/en/4.0/ref/models/querysets/

    #1. 전체 게시글 조회하기 (SELECT * FROM blog_post) 터미널창에 게시글이 조회됨
    #post_list = Post.objects.all()
    #print(post_list)

    # 2. 필터걸기( where 절 사용)
    #post_list = Post.objects.filter(id=1).all()
    #print(post_list)

    # 3. insert(데이터 추가하기)
    #Post.objects.create(
    #    title = "게시글4",
    #    content = "4번째 게시글 입니다"
    #)

    # 전체 게시글을 조회해서 , blog_list.html에 리스트를 rendering 하세요
    #(심화) pagination을 구현하세요
    post_list = Post.objects.all()
# 세션은 서버에 저장함
    
    print('session', request.session.get('cart'))
    if request.session.get('carta'):
        request.session['carta'] = request.session['carta']+["sample"]
    else:
        request.session['carta'] = ['홍진우']

    return render(request, 'blog_list.html',{'post_list':post_list})


#url : /list/<blog_id>  고로 파라미터에 추가
def blog_detail(request, blog_id):

    #블로그 내용을 조회하고 보여주는 페이지 작성(blog_detail.html)
    #(심화) : blog_list 에서 리스트르 클릭하면 해당 페이지로 이동할 수 있도록 하셈
    blog = Post.objects.prefetch_related('comments').get(id=blog_id) # 조인 해서 갖고옴
    # comment 조회
    #blog = Post.objects.get(id=blog_id)

    # print('blog', blog)
    # print('comment', blog.comments.all())
    # print('blog', blog.comments.all()[0].post)
   # Comment.objects.filter(post_id=blog_id).all
   #실습: 7-25
    #1. 댓글을 작성할 수 있도록 구현
    print(request.user)
    return render(request,'blog_detail.html',{'blog':blog})
# 아~ 게시글 작성 하고 싶다
# request.post를 사용해야한다. 그리고 그 내용을 블로그 리스트에 반영(리다이렉트)하기위해 Post.objects.create(블로그 리스트의 {{ post.title }}부분을 사용해서 제목을 반영했으니 title=data['title'])

def comment_post(request,blog_id):# 댓글 기능 구현
    if request.method !='POST' or not request.POST.get('content'):
        return redirect('blog_detail', blog_id=blog_id)
    
    Comment.objects.create(
        content = request.POST['content'],
        post_id = blog_id
    )
    return redirect('blog_detail', blog_id = blog_id)    


def blog_post(request):
    form =PostForm()
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        # data = request.POST
        # board = Post.objects.create(title = data['title'],content=data['content'])
            return redirect("blog_list")

    return render(request, "blog_post.html",{'form': form})


def user_like_post(request):
    if request.method == 'POST':
        UserLikePost.objects.create(
            post_id=request.POST.get('blog_id'),
            user=request.user
        )
    return redirect('blog_list')

    #유저가 좋아요 누른 게시물은 (좋아요 취소로 보이도록 변경)