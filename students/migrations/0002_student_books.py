# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookstudentrelationship'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='books',
            field=models.ManyToManyField(through='books.BookStudentRelationship', to='books.Book'),
        ),
    ]
