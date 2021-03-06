# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20180121_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='city',
            field=models.CharField(blank='True', max_length=15),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='zipcode',
            field=models.CharField(blank='True', max_length=6),
        ),
    ]
