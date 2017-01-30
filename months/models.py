from __future__ import unicode_literals

from django.db import models

class Month(models.Model):
    number = models.IntegerField(blank=False, null=False)
    description = models.CharField(blank=False, null=False, max_length=140)

    def __str__(self):
        return "%s" %(self.description)

    class Meta:
        verbose_name = 'Month'
        verbose_name_plural = 'Months'
        ordering = ('id', )
