from django.db import models
from datetime import datetime
class Realtor(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    title = models.CharField(max_length=15)
    email = models.EmailField()
    hired_date = models.DateTimeField(default=datetime.now, blank=True)
    phone_no = models.CharField(max_length=15)
    realtor_image = models.ImageField(upload_to="photo/%Y/%m/%d", null=True)
    description = models.CharField(max_length=200)
    seller_of_month = models.BooleanField(default=False)
    def __str__(self):
        return self.first_name

