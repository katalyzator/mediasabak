# coding=utf-8
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.encoding import smart_unicode


class Video(models.Model):
    class Meta:
        verbose_name_plural = 'Видео'

    name = models.CharField(max_length=255, verbose_name='Название видео')
    link = models.CharField(max_length=255, verbose_name='Ссылка на видео')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class LessonType(models.Model):
    class Meta:
        verbose_name_plural = 'Категории урока'

    name = models.CharField(max_length=255, verbose_name='Название категории')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class ImageSlide(models.Model):
    class Meta:
        verbose_name_plural = 'Slider Image'
        verbose_name = 'Slider Image'

    name = models.CharField(max_length=255, verbose_name='name of slide')
    image = models.ImageField(upload_to='images/slider', verbose_name='image')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    class Meta:
        verbose_name_plural = 'Уроки'

    name = models.CharField(max_length=255, verbose_name='Название видео')
    link = models.CharField(max_length=255, verbose_name='Ссылка на видео')
    text_type = RichTextUploadingField(verbose_name='Текст урока')
    lesson_type = models.ForeignKey(LessonType, verbose_name='Выберите категорию видеоурока')
    audio = models.FileField(upload_to='files/audio', verbose_name='audiofile')
    imageslide = models.ManyToManyField(ImageSlide, verbose_name='slider image 765x410')
    test = models.ManyToManyField('LessonTest', verbose_name='Выберите тест', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class Test(models.Model):
    class Meta:
        verbose_name_plural = 'Тесты'
        verbose_name = 'Тест'

    name = models.CharField(max_length=500, verbose_name='Вопрос теста')
    image = models.ImageField(upload_to='images/test', verbose_name='Картинка для теста')
    true = models.BooleanField(verbose_name='Фейк')
    false = models.BooleanField(verbose_name='Не Фейк')
    test = models.ForeignKey('LessonTest', verbose_name='Выберите тесты', blank=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class LessonTest(models.Model):
    class Meta:
        verbose_name_plural = 'Тесты для уроков'
        verbose_name = 'Тест'

    name = models.CharField(max_length=500, verbose_name='Название')
    check = models.CharField(max_length=255, default='test', blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.name)
