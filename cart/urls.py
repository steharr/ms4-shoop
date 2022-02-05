from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='cart'),
    path('add/<shoe_id>/', views.add_to_cart, name="add_to_cart"),
    path('remove/<shoe_id>/', views.remove_from_cart, name="remove_from_cart"),
    path('update/<shoe_id>/', views.update_cart, name="update_cart"),
]
