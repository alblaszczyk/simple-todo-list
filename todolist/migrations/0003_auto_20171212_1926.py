# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-12 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20171209_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todolist.ToDoList'),
        ),
    ]
