# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-09 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
    ]
