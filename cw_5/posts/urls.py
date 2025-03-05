from django.urls import path
from .views import edit_post, login_view, logout_view, posts_list, my_posts, post_detail, create_post, delete_post
from .views import register_view
from .views import all_posts

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('posts/', posts_list, name='posts_list'),
    path('posts/my/', my_posts, name='my_posts'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('posts/new/', create_post, name='create_post'),
    path('posts/<int:id>/delete/', delete_post, name='delete_post'),
    path('posts/<int:id>/edit/', edit_post, name='edit_post'),
    path("register/", register_view, name="register"),
    path("posts/my/", my_posts, name="my_posts"),
    path("posts/", all_posts, name="all_posts"),

    

]