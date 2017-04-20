from django.db import models
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True,null=True)
    birth_date = models.DateField(blank=True, null=True)

class Name(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()


