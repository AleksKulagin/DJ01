
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Главная страница
    path('data/', views.data, name='data'),  # Страница data
    path('test/', views.test, name='test'),  # Страница test

]
