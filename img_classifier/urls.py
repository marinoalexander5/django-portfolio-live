from django.urls import path
from . import views


app_name = 'img_classifier'

urlpatterns = [
    path('', views.index, name='main')
]
