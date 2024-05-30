from django.db import models

# Create your models here.

class Regstration(models.Model):
    Username =models.CharField(max_length=50)
    Email =models.EmailField()
    Password=models.CharField(max_length=50)
    Cpassword=models.CharField(max_length=50)
    
    
    def __str__(self):
        return  self.Email
    

class Notes(models.Model):
    Title=models.CharField(max_length=50)
    Note=models.CharField(max_length=200)
    Email=models.EmailField(null=True)
    Password=models.CharField(max_length=50, null=True)
    Date=models.DateField(auto_now=True)