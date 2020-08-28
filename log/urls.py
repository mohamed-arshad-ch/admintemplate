from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register',views.register),
    path('home',views.home),
    path('logout',views.logout),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('update/<int:id>/',views.update,name="update"),
    
  
]