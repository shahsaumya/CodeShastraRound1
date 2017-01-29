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

class HelpGiver(models.Model):
	name = models.CharField(max_length = 30,default='')
	address = models.CharField(max_length = 100,default='')
	capacity=models.IntegerField(default=None)
	lat = models.FloatField(default=None)
	lon = models.FloatField(default=None)


class GroupDetails(models.Model):
	data_token=models.BigIntegerField(default=None)
	number=models.IntegerField(default=None)
	lat = models.FloatField(default=None)
	lon = models.FloatField(default=None)
	individuals=models.ForeignKey(IndividualDetails,on_delete=models.CASCADE,default=None)
	

class IndividualDetails(models.Model):
	name=models.CharField(max_length=30,default='')
	age=models.IntegerField(default=None)
	gender=models.BooleanFiled(default=None)
	key=models.IntegerField(default=None)	











