# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-26 19:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ACCOUNTS', '0006_auto_20161025_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professordetail',
            old_name='Interest',
            new_name='Interests',
        ),
    ]
