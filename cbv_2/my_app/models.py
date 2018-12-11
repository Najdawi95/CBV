# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # for create school view
    def get_absolute_url(self):
        return reverse("my_app:detail", kwargs={'pk': self.pk})  # after create go to detail with this PK


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students')

    def __str__(self):
        return self.name
