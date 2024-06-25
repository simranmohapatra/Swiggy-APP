from django.db import models

# Create your models here.
class A (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=8)