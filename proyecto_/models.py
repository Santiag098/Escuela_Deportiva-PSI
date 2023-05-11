from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    code = models.TextField()
    phone = models.IntegerField()
    description = models.TextField()