from django.db import models

class Transaction_History(models.Model):
    amount = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(max_length=255,null=True,blank=True)

    def get_absolute_url(self):
        return reverse("stage:Thanks_Page")

    def __str__(self):
        return self.order_id
