# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-09 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_infouser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zipcode',
            field=models.IntegerField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
