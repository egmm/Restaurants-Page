# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from list.models import Restaurant

class Comment(models.Model):
    """A simple comment"""
    comment = models.TextField(blank=True)
    pub_date = models.DateTimeField(blank=True, default=timezone.now)
    rate = models.IntegerField(blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment + str(self.rate)
