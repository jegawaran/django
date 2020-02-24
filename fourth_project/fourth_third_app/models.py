from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=264,unique=True)
    lastname = models.CharField(max_length=264,unique=True)
    email = models.EmailField()
    
    def __str__(self):
        return self.firstname