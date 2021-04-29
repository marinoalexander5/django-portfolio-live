from django.db import models
from PIL import Image as Img

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='img_classifier/', blank=True)
    prediction_label = models.CharField(max_length=50, blank=True)
    prediction_value = models.DecimalField(max_digits=4, decimal_places=2, blank=True, default=0)

    # def save(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)

	# 	img = Img.open(self.image.path)

	# 	if img.height > 300 or img.width > 300:
	# 		output_size = (300, 300)
	# 		img.thumbnail(output_size)
	# 		img.save(self.image.path)