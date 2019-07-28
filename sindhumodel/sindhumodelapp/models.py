from django.db import models

# Create your models here.
class Worldcup(models.Model):
    country1=models.CharField(max_length=64)
    country2=models.CharField(max_length=64)
    date=models.DateField()
    result=models.CharField(max_length=64)
