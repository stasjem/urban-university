from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=80)
    balance = models.DecimalField(decimal_places=10, max_digits=19)
    age = models.IntegerField()

class Game(models.Model):
    title = models.CharField(max_length=80)
    cost = models.DecimalField(decimal_places=10, max_digits=19)
    size = models.DecimalField(decimal_places=10, max_digits=19)
    description = models.CharField(max_length=255)
    age_limited = models.BooleanField(False)
    buyer = models.ManyToManyField(Buyer)
