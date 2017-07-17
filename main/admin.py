from django.contrib import admin

from .models import *


class LessonAdmin(admin.ModelAdmin):
    class Meta:
        model = Video


admin.site.register(Video, LessonAdmin)
