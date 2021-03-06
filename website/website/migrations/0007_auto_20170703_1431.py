# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_comment_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('link', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='package',
            name='is_promotional',
            field=models.BooleanField(default=False),
        ),
    ]
