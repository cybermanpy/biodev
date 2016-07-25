from __future__ import unicode_literals

from django.db import models
from usersinfo.models import Userinfo

# Create your models here.

class Speday(models.Model):
    userid = models.ForeignKey(Userinfo, models.DO_NOTHING, db_column='userid')
    startspecday = models.DateTimeField()
    endspecday = models.DateTimeField(blank=True, null=True)
    dateid = models.IntegerField()
    yuanying = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_speday'
        #unique_together = (('userid', 'startspecday', 'dateid'),)