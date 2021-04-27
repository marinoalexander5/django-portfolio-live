from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='img_classifier/', blank=True)
    prediction_label = models.CharField(max_length=50, blank=True)
    prediction_value = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0)