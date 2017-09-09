# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_auto_20170821_2216'),
        ('books', '0003_booktechrelationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='lessons',
            field=models.ManyToManyField(through='lessons.LessonBookRelationship', to='lessons.Lesson'),
        ),
    ]
