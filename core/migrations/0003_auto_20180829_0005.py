# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180829_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateField(blank=True, editable=False, null=True),
        ),
    ]