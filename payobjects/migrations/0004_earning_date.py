# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-31 10:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payobjects', '0003_earning_fkline'),
    ]

    operations = [
        migrations.AddField(
            model_name='earning',
            name='date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2017, 1, 31, 10, 53, 17, 533744, tzinfo=utc)),
            preserve_default=False,
        ),
    ]