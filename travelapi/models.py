from django.db import models

# Create your models here.

class BookingModel(models.Model):
	name=models.CharField(max_length=20)
	person=models.CharField(max_length=2)
	place=models.TextField()
	price=models.IntegerField()
	date=models.TextField()
