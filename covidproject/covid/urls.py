from .import views
from django.urls import path

urlpatterns = [
    path('', views.demo,name="demo"),
    path('add/', views.add_movie, name='add_movie'),


]
