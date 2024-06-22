from django.contrib import admin
from django.urls import path, re_path
from .views import *
from django.conf.urls.static import static, serve
from django.conf import settings

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
] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
                re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]
