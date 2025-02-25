from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def thread_list(request):
    threads = Thread.objects.all()
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm()
    return render(request, 'post/thread_list.html', {'threads': threads, 'form': form})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=id)
    else:
        form = PostForm()
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})

def delete_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread_list')

def edit_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == "POST":
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'post/edit_thread.html', {'form': form})

def delete_post(request, thread_id, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('thread_detail', id=thread_id)

def edit_post(request, thread_id, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=thread_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/edit_post.html', {'form': form})
