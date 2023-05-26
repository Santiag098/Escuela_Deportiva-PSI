from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    code = models.TextField()
    phone = models.IntegerField()
    description = models.TextField()
    
def __str__(self):
    return self.name


class Pay(models.Model):
    credit_num=models.IntegerField(max_length=16)
    due_date= models.TextField(default=0)
    security_code= models.IntegerField(max_length=10)
    amount_paid=models.FloatField(default=0)
    description= models.CharField(max_length=200)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, default=1)
    
def __str__(self):
    return self.name


