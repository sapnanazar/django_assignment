
from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('home/', admin.site.urls),
    path('', views.home),
    
    path('home/', views.index, name='index'),
    path('index/', views.index, name='index'),
]
