from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', render_main, name='index'),
    path('detail/<int:pk>/', render_detail, name='detail'),
    path('explore/', render_explore, name='explore'),
    path('create/', render_create, name='create'),
    path('login/', render_login, name='login'),
    path('logout/', render_logout, name='logout'),
    path('register/', render_register, name='register'),
]
