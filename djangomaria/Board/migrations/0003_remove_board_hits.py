# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0002_auto_20170113_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='hits',
        ),
    ]
