# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-03 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20151021_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='personpage',
            name='telephone_2',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
