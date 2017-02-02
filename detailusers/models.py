from __future__ import unicode_literals

from django.db import models
from usersinfo.models import Userinfo

class Detailuser(models.Model):
    line = models.IntegerField(blank=False, null=False, default=0)
    email = models.EmailField(blank=True, null=True)
    fkuserinfo = models.OneToOneField(Userinfo)

    def __str__(self):
        return  ("%s") %(self.line)

    class Meta:
        verbose_name = 'Detail User'
        verbose_name_plural = 'Detail Users'
        ordering = ('id',)