from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from myapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),

    path('news/', include('news.urls')),

    path('', views.home, name='home'),  # Главная страница
    path('data/', views.data, name='data'),  # Страница data
    path('test/', views.test, name='test'),  # Страница test
    path('test2/', views.test2, name='test2'),  # Страница test2
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
