from django.db import models
from PIL import Image
from keras.preprocessing.image import img_to_array
import cv2
import numpy as np
from .apps import DigitClassifierConfig

# Create your models here.
class Digit(models.Model):
    image = models.ImageField(upload_to='digits')
    result = models.CharField(max_length=2, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        print(self.image)
        img = Image.open(self.image)
        img_array = img_to_array(img)
        print(img_array.shape)
        dims = (28, 28)
        img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        img_array = cv2.resize(img_array, dims, interpolation=cv2.INTER_AREA)
        img_array = np.expand_dims(img_array, axis=(0, 3))
        print(img_array.shape)

        try:
            loaded_model = DigitClassifierConfig.mlmodel
            pred = np.argmax(loaded_model.predict(img_array))
            self.result = str(pred)
            print(f'classified as {pred}')
        except:
            print('failed to classify')
            self.result = 'failed to classify'

        return super().save(*args, **kwargs)