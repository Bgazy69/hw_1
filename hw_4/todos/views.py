from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def home(request):
    return redirect('todo_lists')

def todo_lists(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/todo_lists.html', {'todo_lists': todo_lists})

def create_todo_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_lists')
    else:
        form = TodoListForm()
    return render(request, 'todos/todo_lists.html', {'form': form})

def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_list_details', id=id)
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'todos/edit_todo_list.html', {'form': form})

def todo_list_details(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = Todo.objects.filter(todo_list=todo_list)
    return render(request, 'todos/todo_list_details.html', {'todo_list': todo_list, 'todos': todos})

def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo_lists')

def create_todo(request, todo_list_id):
    todo_list = get_object_or_404(TodoList, id=todo_list_id)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect('todo_list_details', id=todo_list_id)
    else:
        form = TodoForm()
    return render(request, 'todos/todo_list_details.html', {'form': form, 'todo_list': todo_list})

def edit_todo(request, todo_list_id, id):
    todo = get_object_or_404(Todo, id=id, todo_list__id=todo_list_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list_details', id=todo_list_id)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form, 'todo_list_id': todo_list_id})

def delete_todo(request, todo_list_id, id):
    todo = get_object_or_404(Todo, id=id, todo_list__id=todo_list_id)
    todo.delete()
    return redirect('todo_list_details', id=todo_list_id)
