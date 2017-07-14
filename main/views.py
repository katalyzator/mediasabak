from django.shortcuts import render


def index_view(request):
    context = {}
    template = 'index.html'

    return render(request, template, context)


def lesson_page_view(request):
    context = {}
    template = 'lesson-page.html'

    return render(request, template, context)


def video_lesson_view(request):
    context = {}
    template = 'video-lessons.html'

    return render(request, template, context)
