# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-15 16:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACCOUNTS', '0003_auto_20161114_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentdetail',
            name='CreationDate',
            field=models.DateField(default=datetime.date(2016, 11, 15)),
        ),
    ]
