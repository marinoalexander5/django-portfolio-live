from django.urls import path
from . import views as crypto_tracker_views

app_name= 'crypto-tracker'
urlpatterns = [
    path('', crypto_tracker_views.home, name='main'),
]
