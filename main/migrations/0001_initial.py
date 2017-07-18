# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-18 16:29
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name of slide')),
                ('image', models.ImageField(upload_to='images/slider', verbose_name='image')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Slider Image',
                'verbose_name_plural': 'Slider Image',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u0438\u0434\u0435\u043e')),
                ('link', models.CharField(max_length=255, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e')),
                ('text_type', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0443\u0440\u043e\u043a\u0430')),
                ('audio', models.FileField(upload_to='files/audio', verbose_name='audiofile')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('imageslide', models.ManyToManyField(to='main.ImageSlide', verbose_name='slider image 765x410')),
            ],
            options={
                'verbose_name_plural': '\u0423\u0440\u043e\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='LessonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0443\u0440\u043e\u043a\u0430',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u0438\u0434\u0435\u043e')),
                ('link', models.CharField(max_length=255, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0432\u0438\u0434\u0435\u043e')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e',
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.LessonType', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u0432\u0438\u0434\u0435\u043e\u0443\u0440\u043e\u043a\u0430'),
        ),
    ]
