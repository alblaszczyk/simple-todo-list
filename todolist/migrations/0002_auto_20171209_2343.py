# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-09 23:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='todo',
            new_name='todo_list',
        ),
    ]