from django.apps import AppConfig
from keras.applications.vgg16 import VGG16

class ImgClassifierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'img_classifier'

    # Load classification model
    model = VGG16()