from __future__ import unicode_literals
from django.db import models
from usersinfo.models import Userinfo
from months.models import Month
from years.models import Year

class PayObject(models.Model):
    number = models.IntegerField(blank=False, null=False)
    concept = models.CharField(blank=False, null=False, max_length=140)
    pays = models.ManyToManyField(Userinfo, through='Earning')

    def __str__(self):
        return "%s" %(self.number)

    class Meta:
        verbose_name = 'PayObject'
        verbose_name_plural = 'PayObjects'
        ordering = ('id', )

class Earning(models.Model):
    fkuserinfo = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    fkpayobject = models.ForeignKey(PayObject, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, null=False)
    fkmonth = models.ForeignKey(Month, on_delete=models.CASCADE)
    fkyear = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" %(self.fkuserinfo)

    class Meta:
        verbose_name = 'Earning'
        verbose_name_plural = 'Earnings'
        ordering = ('id', )