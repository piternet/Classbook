# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-15 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20180614_2211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['date']},
        ),
    ]
