from django.contrib import admin
from .models import Listing
from django.db import models




class Listing_admin(admin.ModelAdmin):
    list_display = ('title', 'address', 'city', 'state', 'zip', 'price')
    list_display_links = ('title','address','city','state','zip','price')
    list_filter = ('title', 'city')

admin.site.register(Listing,Listing_admin)