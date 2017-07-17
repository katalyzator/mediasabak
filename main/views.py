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
    videos = Video.objects.all()
    context = {"lessons": videos}
    template = 'video-lessons.html'

    return render(request, template, context)
