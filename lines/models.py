from __future__ import unicode_literals

from django.db import models

class Line(models.Model):
    number = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return  ("%s") %(self.number)

    class Meta:
        verbose_name = 'Linea'
        verbose_name_plural = 'Lineas'
        ordering = ('id',)