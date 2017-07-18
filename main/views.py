from django.shortcuts import render

from .models import *


def index_view(request):
    context = {}
    template = 'index.html'

    return render(request, template, context)


def lesson_page_view(request):
    lesson = Lesson.objects.all()
    context = {}
    template = 'lesson-page.html'

    return render(request, template, context)


def video_lesson_view(request):
    videos = Video.objects.all()
    context = {"lessons": videos}
    template = 'video-lessons.html'

    return render(request, template, context)


def education_view(request):
    context = {}
    template = 'education.html'

    return render(request, template, context)


def about_view(request):
    context = {}
    template = 'about.html'

    return render(request, template, context)


def more_view(request):
    context = {}
    template = 'more-information.html'

    return render(request, template, context)
