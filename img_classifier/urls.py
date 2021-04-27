from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'img_classifier'

urlpatterns = [
    path('', views.index, name='main')
]