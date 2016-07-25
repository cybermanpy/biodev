from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Department(models.Model):
    deptid = models.AutoField(primary_key=True)
    deptname = models.CharField(max_length=30, blank=True, null=True)
    supdeptid = models.IntegerField()
    inheritparentsch = models.IntegerField(blank=True, null=True)
    inheritdeptsch = models.IntegerField(blank=True, null=True)
    inheritdeptschclass = models.IntegerField(blank=True, null=True)
    autoschplan = models.IntegerField(blank=True, null=True)
    inlate = models.IntegerField(blank=True, null=True)
    outearly = models.IntegerField(blank=True, null=True)
    inheritdeptrule = models.IntegerField(blank=True, null=True)
    minautoschinterval = models.IntegerField(blank=True, null=True)
    registerot = models.IntegerField(blank=True, null=True)
    defaultschid = models.IntegerField(blank=True, null=True)
    att = models.IntegerField(blank=True, null=True)
    holiday = models.IntegerField(blank=True, null=True)
    overtime = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.deptname
    
    class Meta:
        managed = False
        db_table = 'departments'