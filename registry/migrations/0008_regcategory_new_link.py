# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0007_auto_20171001_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='regcategory',
            name='new_link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
