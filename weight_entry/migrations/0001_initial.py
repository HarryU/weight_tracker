# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 19:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True)),
                ('weight', models.FloatField()),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
    ]
