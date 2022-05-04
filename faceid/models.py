from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=100)
    photo = photo = models.ImageField(upload_to='access_control/cars')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

