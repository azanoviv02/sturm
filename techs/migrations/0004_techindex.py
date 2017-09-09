# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 23:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('techs', '0003_techstudentrelationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]