from django.db import models

class Employee(models.Model):
# Create your models here.
    name = models.CharField(max_length=123,null=False)
    age = models.IntegerField(null=False)
    address = models.CharField(max_length=300,null=False)
    place = models.TextField(null=False)
    email_id = models.EmailField(null=False)