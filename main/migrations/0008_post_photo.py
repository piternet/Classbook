# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-12 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180119_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='main/static/main/imgs/'),
        ),
    ]
