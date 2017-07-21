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


class TestInline(admin.StackedInline):
    model = Test
    max_num = 200
    extra = 0


class LessonTestInline(admin.ModelAdmin):
    inlines = [TestInline, ]


class TestAdmin(admin.ModelAdmin):
    class Meta:
        model = Test


admin.site.register(LessonTest, LessonTestInline)

admin.site.register(Test, TestAdmin)

admin.site.register(ImageSlide, SliderImageAdmin)

admin.site.register(LessonType, LessonTypeInline)

admin.site.register(Lesson, LessonAdmin)

admin.site.register(Video, VideoAdmin)
