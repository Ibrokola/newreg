# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional', '0008_auto_20170930_0604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calender',
            name='pos',
        ),
        migrations.AddField(
            model_name='calender',
            name='order',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
