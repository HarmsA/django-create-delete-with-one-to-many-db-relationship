# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-05 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20181205_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher',
            new_name='t_name',
        ),
    ]