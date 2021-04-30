from django.apps import AppConfig
from keras.applications.mobilenet import MobileNet

class ImgClassifierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'img_classifier'

    # Load classification model
    model = MobileNet()