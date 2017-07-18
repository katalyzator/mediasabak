from django.contrib import admin

from .models import *


class VideoAdmin(admin.ModelAdmin):
    class Meta:
        model = Video


class LessonAdmin(admin.ModelAdmin):
    class Meta:
        model = Lesson


class LessonInline(admin.StackedInline):
    model = Lesson
    max_num = 200
    extra = 0


class LessonTypeInline(admin.ModelAdmin):
    inlines = [LessonInline, ]


class SliderImageAdmin(admin.ModelAdmin):
    class Meta:
        model = ImageSlide


admin.site.register(ImageSlide, SliderImageAdmin)

admin.site.register(LessonType, LessonTypeInline)

admin.site.register(Lesson, LessonAdmin)

admin.site.register(Video, VideoAdmin)
