from django.contrib import admin

from .models import *


class VideoAdmin(admin.ModelAdmin):
    class Meta:
        model = Video


class LessonAdmin(admin.ModelAdmin):
    class Meta:
        model = Lesson


admin.site.register(Lesson, LessonAdmin)

admin.site.register(Video, VideoAdmin)
