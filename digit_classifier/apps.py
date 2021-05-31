from django.apps import AppConfig
import os
from django.conf import settings
from tensorflow.keras.models import load_model


class DigitClassifierConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'digit_classifier'

    # Load classification model
    MLMODEL_FOLDER = os.path.join(settings.BASE_DIR, 'digit_classifier/mlmodels/')
    MLMODEL_FILE = os.path.join(MLMODEL_FOLDER, 'digit_classifier_model.h5')
    mlmodel = load_model(MLMODEL_FILE)
