# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-10 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
