from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length = 20)
	address = models.CharField(max_length = 50)
	emergency_contact = models.CharField(max_length = 20)
	emergency_no = models.IntegerField()
	disaster = models.CharField(max_length = 20)
	lat = models.FloatField()
	lon = models.FloatField()

