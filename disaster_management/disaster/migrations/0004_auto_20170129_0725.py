# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-29 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster', '0003_auto_20170129_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='data_token',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
