from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Post
from .forms import LoginForm, PostForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("posts_list")
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("posts_list")
    else:
        form = AuthenticationForm()
    
    return render(request, "login.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("posts_list")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def posts_list(request):
    posts = Post.objects.all()
    return render(request, "posts_list.html", {"posts": posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, "posts/my_posts.html", {"posts": posts})

@login_required
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post_detail.html", {"post": post, "can_edit": post.author == request.user or request.user.is_superuser})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("posts_list")
    else:
        form = PostForm()
    
    return render(request, "posts/create_post.html", {"form": form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
    return redirect("posts_list")

@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Проверяем, что только автор или суперюзер может редактировать
    if request.user != post.author and not request.user.is_superuser:
        return redirect("posts_list")
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", id=post.id)
    else:
        form = PostForm(instance=post)
    
    return render(request, "edit_post.html", {"form": form, "post": post})

def all_posts(request):
    posts = Post.objects.all().order_by("-id")  # Сортируем по убыванию, чтобы новые посты были первыми
    return render(request, "posts/all_posts.html", {"posts": posts})