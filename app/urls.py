from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', render_main, name='index'),
]
