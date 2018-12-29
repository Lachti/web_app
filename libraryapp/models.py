# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default=None, blank=True, null=True)
    year_published = models.IntegerField(default=None, blank=True, null=True)
    is_rented = models.BooleanField(default=False)
    
    def __unicode__(self):
        return 'Title: ' + self.title + ' | Author: ' + self.author + ' | Year: ' + str(self.year_published)

class Rental(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return 'Username: ' + str(self.user) + ' | BookID: ' + str(self.book.id) + ' | Active: ' + str(self.is_active)
