# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    course = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=8)

    def __str__(self):
        return self.name + ' - ' + self.price 
