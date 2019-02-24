from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    
    def __str__(self):
    	return self.firstname

class Expense(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField()
	category = models.TextField(default='')
	detail = models.TextField(default='')
	place = models.TextField(default='')
	amount = models.FloatField(default=0.0)

	def __str__(self):
		return self.detail

class Balance(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	currency = models.CharField(max_length=3, default='$')
	income = models.IntegerField(default=0)
	expense = models.IntegerField(default=0)
	rest = models.IntegerField(default=0)
	saving = models.IntegerField(default=0)

	def __str__(self):
		return str(self.rest)