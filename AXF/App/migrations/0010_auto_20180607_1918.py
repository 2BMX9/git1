# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-07 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_order_ordergoods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
