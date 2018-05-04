
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class coordinates(models.Model):
    lat= models.CharField(max_length=250)
    lon = models.CharField(max_length=250)
    speed=models.CharField(max_length=250)
    x = models.CharField(max_length=250)
    y = models.CharField(max_length=250)
    z = models.CharField(max_length=250)
    ultra = models.CharField(max_length=250)
    smoke=models.CharField(max_length=250)
    heart = models.CharField(max_length=250)    
        
