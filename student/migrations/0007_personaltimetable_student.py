# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 03:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20160508_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaltimetable',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
            preserve_default=False,
        ),
    ]