# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-14 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invest', '0002_stocks_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='quantity',
            field=models.BigIntegerField(default=12),
            preserve_default=False,
        ),
    ]