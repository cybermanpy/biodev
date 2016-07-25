from __future__ import unicode_literals

from django.db import models
from departments.models import Department
# Create your models here.

class Userinfo(models.Model):
    userid = models.AutoField(primary_key=True)
    badgenumber = models.CharField(unique=True, max_length=24)
    ssn = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=8, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    pager = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)
    hiredday = models.DateTimeField(blank=True, null=True)
    street = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=2, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=12, blank=True, null=True)
    ophone = models.CharField(max_length=20, blank=True, null=True)
    fphone = models.CharField(max_length=20, blank=True, null=True)
    verificationmethod = models.IntegerField(blank=True, null=True)
    defaultdeptid = models.ForeignKey(Department, models.DO_NOTHING, db_column='defaultdeptid', blank=True, null=True)
    #defaultdeptid_id = models.ForeignKey(Department)
    securityflags = models.IntegerField(blank=True, null=True)
    att = models.IntegerField()
    inlate = models.IntegerField()
    outearly = models.IntegerField()
    overtime = models.IntegerField()
    sep = models.IntegerField()
    holiday = models.IntegerField()
    minzu = models.CharField(max_length=8, blank=True, null=True)
    lunchduration = models.IntegerField()
    mverifypass = models.CharField(max_length=10, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    inheritdeptsch = models.IntegerField(blank=True, null=True)
    inheritdeptschclass = models.IntegerField(blank=True, null=True)
    autoschplan = models.IntegerField(blank=True, null=True)
    minautoschinterval = models.IntegerField(blank=True, null=True)
    registerot = models.IntegerField(blank=True, null=True)
    inheritdeptrule = models.IntegerField(blank=True, null=True)
    emprivilege = models.IntegerField(blank=True, null=True)
    cardno = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    privilege = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'userinfo'

# class Checkinout(models.Model):
#     userid = models.ForeignKey(Userinfo, models.DO_NOTHING, db_column='userid')
#     checktime = models.DateTimeField()
#     checktype = models.CharField(max_length=1, blank=True, null=True)
#     verifycode = models.IntegerField(blank=True, null=True)
#     sensorid = models.CharField(max_length=5, blank=True, null=True)
#     workcode = models.IntegerField(blank=True, null=True)
#     sn = models.CharField(max_length=20, blank=True, null=True)
#     userextfmt = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'checkinout'
#         unique_together = (('userid', 'checktime'),)