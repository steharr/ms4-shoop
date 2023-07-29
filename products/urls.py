from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_shoes, name="shoes"),
    path('<int:shoe_id>', views.shoe_detail, name="shoe_detail"),
]
