# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
