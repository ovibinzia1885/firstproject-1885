from django.db import models
from datetime import datetime
from django.utils import timezone

from Realtors.models import Realtor


class Listing(models.Model):
    realtor= models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    zipcode=models.CharField(max_length=150)
    des2 = models.TextField(blank=True, verbose_name='Description')
    price=models.IntegerField()
    bedroom=models.IntegerField()
    garage=models.BooleanField()
    sqft=models.IntegerField()
    lot_size=models.DecimalField(decimal_places=2,max_digits=6)
    is_published=models.BooleanField()
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d')
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d')
    list_date=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-list_date',)