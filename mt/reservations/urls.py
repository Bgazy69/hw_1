from django.urls import path
from .views import (
    reservation_list, reservation_detail, reservation_create,
    reservation_edit, reservation_delete
)

urlpatterns = [
    path('', reservation_list, name='reservation_list'),
    path('<int:id>/', reservation_detail, name='reservation_detail'),
    path('create/', reservation_create, name='reservation_create'),
    path('<int:id>/edit/', reservation_edit, name='reservation_edit'),
    path('<int:id>/delete/', reservation_delete, name='reservation_delete'),
]
