# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-22 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170722_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='check',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0442\u0435\u0441\u0442'),
        ),
    ]