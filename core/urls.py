from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'app.views.page_not_found'
handler500 = 'app.views.custom_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
