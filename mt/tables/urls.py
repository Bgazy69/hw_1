from django.urls import path
from .views import table_list, table_create, table_available

urlpatterns = [
    path('', table_list, name='table_list'),
    path('create/', table_create, name='table_create'),
    path('available/', table_available, name='table_available'),
]
