# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projectstudentrelationship'),
        ('students', '0002_student_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='projects',
            field=models.ManyToManyField(through='projects.ProjectStudentRelationship', to='projects.Project'),
        ),
    ]
