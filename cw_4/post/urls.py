from django.urls import path
from . import views

urlpatterns = [
    path('threads/', views.thread_list, name='thread_list'),
    path('threads/<int:id>/', views.thread_detail, name='thread_detail'),
    path('threads/<int:id>/delete/', views.delete_thread, name='delete_confirm'),
    path('threads/<int:id>/edit/', views.edit_thread, name='edit_thread'),
    path('posts/<int:thread_id>/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('posts/<int:thread_id>/<int:id>/edit/', views.edit_post, name='edit_post'),
]