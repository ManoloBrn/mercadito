# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-10 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventarios', '0002_auto_20161209_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
