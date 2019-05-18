from django.db import models
from django.urls import reverse
# Create your models here.

class Words_Bank(models.Model):
    kor_word = models.CharField(max_length=100)
    eng_word = models.CharField(max_length=100)

    def __str__(self):
        return self.kor_word
    def get_absolute_url(self):
        return reverse("helper:Main_Page") #kwargs = {"pk" : self.pk }
