# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 11:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 2, 24, 11, 53, 10, 450031, tzinfo=utc))),
                ('pattern', models.CharField(max_length=100)),
            ],
        ),
    ]
