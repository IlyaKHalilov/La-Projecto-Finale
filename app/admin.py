from django.contrib import admin
from .models import MyPerson, MyPersonDetail


admin.site.register(MyPerson)
admin.site.register(MyPersonDetail)
