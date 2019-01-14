from django.db import models
from django.urls import reverse
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length = 60)
    image = models.FileField(upload_to="detector/Images")
    description = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("detector:On_Success_Page", kwargs={"pk":self.pk})
