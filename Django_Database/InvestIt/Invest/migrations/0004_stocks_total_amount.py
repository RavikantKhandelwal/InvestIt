# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-14 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invest', '0003_stocks_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocks',
            name='total_amount',
            field=models.BigIntegerField(default=122),
            preserve_default=False,
        ),
    ]
