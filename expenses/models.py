from django.db import models

# Create your models here.

class User(models.Model):
    _id = models.CharField(max_length=5)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    # fullname = firstname + ' ' + lastname
    
    def __str__(self):
    	return self.firstname