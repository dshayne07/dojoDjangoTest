from __future__ import unicode_literals

from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="dojo_id")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)