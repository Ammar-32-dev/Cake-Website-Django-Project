from django.urls import path
from . import views  # Ensure you import views from the current directory

urlpatterns = [
    path('', views.cake_list, name='cake_list'),
    path('cake/<int:id>/', views.cake_detail, name='cake_detail'),
    path('order/', views.place_order, name='place_order'),
    path('order/<int:id>/confirmation/', views.order_confirmation, name='order_confirmation'),
]
