from django.urls import path
from . import views

app_name= 'jsprojects'
urlpatterns = [
    path('', views.home, name='main'),
    path('background-color/', views.bg_color, name='bg-color'),
    path('background-video/', views.bg_video, name='bg-video'),
]