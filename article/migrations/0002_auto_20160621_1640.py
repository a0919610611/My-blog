# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 08:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='stauts',
            new_name='status',
        ),
    ]
