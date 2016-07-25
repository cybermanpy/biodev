from __future__ import unicode_literals

from django.db import models
from usersinfo.models import Userinfo

# Create your models here.

class Check(models.Model):
    # userid = models.ForeignKey(Userinfo)
    userid = models.ForeignKey(Userinfo, models.DO_NOTHING, db_column='userid')
    checktime = models.DateTimeField()
    checktype = models.CharField(max_length=1, blank=True, null=True)
    verifycode = models.IntegerField(blank=True, null=True)
    sensorid = models.CharField(max_length=5, blank=True, null=True)
    workcode = models.IntegerField(blank=True, null=True)
    sn = models.CharField(max_length=20, blank=True, null=True)
    userextfmt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkinout'
        # unique_together = (('userid', 'checktime'),)
        # unique_together = ['userid', 'checktime']