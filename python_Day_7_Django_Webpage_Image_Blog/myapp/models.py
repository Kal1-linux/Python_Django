from django.db import models

# Create your models here.
class Emp(models.Model):
    uname=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=10)
