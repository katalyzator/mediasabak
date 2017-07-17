from django.shortcuts import render

from .models import *


def index_view(request):
    context = {}
    template = 'index.html'

    return render(request, template, context)


def lesson_page_view(request):
    context = {}
    template = 'lesson-page.html'

    return render(request, template, context)


def video_lesson_view(request):
    lessons = Lesson.objects.all()
    context = {"lessons": lessons}
    template = 'video-lessons.html'

    return render(request, template, context)
