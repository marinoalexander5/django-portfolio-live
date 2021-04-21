from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='img_classifier/')
    prediction = models.CharField(max_length=50, blank=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)