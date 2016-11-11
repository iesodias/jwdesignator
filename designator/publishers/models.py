from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    group = models.CharField(max_length=30)
    car = models.CharField(max_length=30)