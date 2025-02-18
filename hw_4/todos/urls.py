from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo-lists/', views.todo_lists, name='todo_lists'),
    path('todo-lists/create/', views.create_todo_list, name='create_todo_list'),
    path('todo-lists/<int:id>/', views.todo_list_details, name='todo_list_details'),
    path('todo-lists/<int:id>/edit/', views.edit_todo_list, name='edit_todo_list'),
    path('todo-lists/<int:id>/delete/', views.delete_todo_list, name='delete_todo_list'),
    path('todos/<int:todo_list_id>/create/', views.create_todo, name='create_todo'),
    path('todos/<int:todo_list_id>/<int:id>/edit/', views.edit_todo, name='edit_todo'),
    path('todos/<int:todo_list_id>/<int:id>/delete/', views.delete_todo, name='delete_todo'),
]