from django.db import models
from django.urls import reverse
# Create your models here.

class Task(models.Model):
    content = models.CharField(max_length=255)
    is_checked = models.BooleanField(default=False)

    def action_check(self):
        self.is_checked = not self.is_checked
        self.save()

    def get_absolute_url(self):
        return reverse("hal_il:Main_Page")

    def __str__(self):
        return self.content
