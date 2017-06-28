# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20170628_1129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='days',
            options={'verbose_name': 'Day', 'verbose_name_plural': 'Days'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery', 'verbose_name_plural': 'Galleries'},
        ),
        migrations.AlterModelOptions(
            name='itenary',
            options={'verbose_name': 'Iternary', 'verbose_name_plural': 'Iternaries'},
        ),
        migrations.AlterModelOptions(
            name='package',
            options={'verbose_name': 'Package', 'verbose_name_plural': 'Packages'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Page', 'verbose_name_plural': 'Pages'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Place', 'verbose_name_plural': 'Places'},
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'verbose_name': 'Season', 'verbose_name_plural': 'Seasons'},
        ),
        migrations.AlterField(
            model_name='package',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Gallery'),
        ),
    ]
