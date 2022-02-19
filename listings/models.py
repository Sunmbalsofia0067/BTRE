from django.db import models
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
    # listing_identity = models.BigAutoField()
    title = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    square_feet = models.DecimalField(max_digits=6, decimal_places=2)
    lot_size = models.IntegerField()
    garage = models.IntegerField()
    listing_date = models.DateTimeField()
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=300)
    is_published = models.BooleanField(default=True)
    main_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',null=True,blank=True)
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True,blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True,blank=True)
    image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True,blank=True)
    image_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True,blank=True)

    def __str__(self):
        return self.title