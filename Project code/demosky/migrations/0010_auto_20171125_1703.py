# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demosky', '0009_auto_20171125_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensormine',
            name='date',
            field=models.DateField(),
        ),
    ]
