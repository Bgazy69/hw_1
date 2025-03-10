from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Todo
from .forms import TodoForm

# Логин парағы
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')
    return render(request, 'todos/login.html')

# Логаут функциясы
def logout_view(request):
    logout(request)
    return redirect('login')

# TODO тізімі (тек өзінің Todos-ы көрінеді)
@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/todo_list.html', {'todos': todos})

# Белгілі бір TODO-ны көру
@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

# TODO қосу (Django Forms пайдалану)
@login_required
def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/add_todo.html', {'form': form})

# TODO өшіру
@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect('todo_list')

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)

    if request.method == "POST":
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.due_date = request.POST['due_date']
        todo.status = request.POST['status'] == "True"  # Convert to boolean
        todo.save()
        return redirect('todo_list')

    return render(request, 'todos/edit_todo.html', {'todo': todo})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'todos/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'todos/register.html', {'error': 'Username already taken'})

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        login(request, user)  # Автоматты түрде логин жасау
        return redirect('todo_list')

    return render(request, 'todos/register.html')