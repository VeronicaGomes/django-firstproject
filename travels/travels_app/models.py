from django.db import models

# Create your models here.

class Destination(models.Model):
	
	city    = models.CharField(max_length=100)
	img     = models.ImageField(upload_to='pictures')
	price   = models.IntegerField()
	country = models.CharField(max_length=100)

class Hotel(models.Model):
	name    = models.CharField(max_length=100)
	img     = models.ImageField(upload_to='pictures')
	price   = models.IntegerField()
	country = models.CharField(max_length=100)
	city    = models.CharField(max_length=100)




