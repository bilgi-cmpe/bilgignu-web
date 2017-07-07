# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-07 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arcade', '0003_machine_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]
