# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-22 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_lesson_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='correct',
            field=models.CharField(default=1, max_length=500, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0433\u043e \u043e\u0442\u0432\u0435\u0442\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='incorrect',
            field=models.CharField(default=1, max_length=500, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043d\u0435\u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0433\u043e \u043e\u0442\u0432\u0435\u0442\u0430'),
            preserve_default=False,
        ),
    ]
