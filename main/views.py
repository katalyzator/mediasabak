from django.shortcuts import render

from .models import *


def index_view(request):
    context = {}
    template = 'index.html'

    return render(request, template, context)


def lesson_page_view(request, id):
    all_lesson = Lesson.objects.all().filter(lesson_type_id=id)
    lesson = all_lesson.first()
    sliderimage = ImageSlide.objects.filter(lesson__lesson_type_id=id)
    request.session['id'] = id

    context = {"lesson": lesson, "images": sliderimage, "all_lesson": all_lesson}
    template = 'lesson-page.html'

    return render(request, template, context)


def video_lesson_view(request):
    videos = Video.objects.all()
    context = {"lessons": videos}
    template = 'video-lessons.html'

    return render(request, template, context)


def education_view(request):
    lesson_type1 = LessonType.objects.all().order_by('timestamp')[0:4]
    lesson_type2 = LessonType.objects.all().order_by('timestamp')[4:8]
    context = {"lesson_type1": lesson_type1, "lesson_type2": lesson_type2}
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


def single_lesson(request, id):
    lesson = Lesson.objects.get(id=id)
    all_lesson = Lesson.objects.all().filter(lesson_type_id=request.session['id'])
    sliderimage = ImageSlide.objects.all().filter(lesson=lesson)
    context = {"lesson": lesson, "images": sliderimage, "all_lesson": all_lesson}
    template = 'single-lesson.html'

    return render(request, template, context)


def lesson_test(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    test = Test.objects.all().filter(test__lesson=lesson)
    all_lesson = Lesson.objects.all().filter(lesson_type_id=request.session['id'])
    context = {"test": test, "all_lesson": all_lesson}
    template = 'lesson_test.html'

    return render(request, template, context)


def book_view(request):
    context = {}
    template = 'book.html'

    return render(request, template, context)
