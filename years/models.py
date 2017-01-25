from __future__ import unicode_literals

from django.db import models

class Year(models.Model):
    description = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return "%s" %(self.description)

    class Meta:
        verbose_name = 'Year'
        verbose_name_plural = 'Years'
        ordering = ('id', )