from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', render_main, name='index'),
    path('detail/<int:pk>/', render_detail, name='detail'),
    path('create/', render_create, name='create'),
    path('login/', render_login, name='login'),
    path('logout/', render_logout, name='logout'),
    path('register/', render_register, name='register'),
    path('access_denied/', render_access_denied, name='no_access'),
    path('application/', render_application, name='application'),
    path('view_applications/', render_applications, name='applications'),
    path('update/<int:pk>/', render_update, name='update'),
    path('delete/<int:pk>/', render_delete, name='delete'),
]
