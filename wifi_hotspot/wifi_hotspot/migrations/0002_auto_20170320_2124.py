# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wifi_hotspot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordgeneration',
            name='password_unique',
            field=models.CharField(max_length=100),
        ),
    ]
