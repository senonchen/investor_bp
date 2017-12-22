from __future__ import unicode_literals

from django.db import models

# Create your models here.
class investor(models.Model):
    the_id = models.CharField(max_length=300)
    realname = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    telephone = models.CharField(max_length=300)
    weixin = models.CharField(max_length=300)
    create_time = models.CharField(max_length=300)
    update_time = models.CharField(max_length=300)
    last_login  = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    position  = models.CharField(max_length=300)
    industry  = models.CharField(max_length=300)
    investAmount  = models.CharField(max_length=300)
    fields = models.CharField(max_length=300)
    stages = models.CharField(max_length=300)
    roles = models.CharField(max_length=300)
    ps = models.TextField(max_length=5000)
    """docstring for investor"""
    def __unicode__(self):
        return self.realname

        