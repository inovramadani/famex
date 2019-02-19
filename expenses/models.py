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
	date = models.DateTimeField()
	expense_detail = models.TextField()

	def __str__(self):
		return self.expense_detail