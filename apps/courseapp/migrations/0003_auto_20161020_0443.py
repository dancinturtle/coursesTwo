# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseapp', '0002_auto_20161020_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]