from django.contrib import admin
from .models import MyPerson, MyPersonDetail, Application


admin.site.register(MyPerson)
admin.site.register(MyPersonDetail)
admin.site.register(Application)
