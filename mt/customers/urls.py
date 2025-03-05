from django.urls import path
from .views import customer_list, customer_detail, customer_create

urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('<int:id>/', customer_detail, name='customer_detail'),
    path('create/', customer_create, name='customer_create'),
]