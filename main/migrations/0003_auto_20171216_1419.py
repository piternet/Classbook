# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-16 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171211_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edit_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]