# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20170705_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='discount_code',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
