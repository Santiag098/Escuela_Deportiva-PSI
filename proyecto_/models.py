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
    name = models.CharField(max_length=200)
    code = models.IntegerField(default=0)
    pay_day = models.DateField(default="2023-05-18")
    amount_paid = models.FloatField(default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE, default=1)
    
def __str__(self):
    return self.name


