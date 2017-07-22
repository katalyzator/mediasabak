"""mediasabak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from mediasabak import settings

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', 'main.views.index_view', name='index'),
    url(r'^lessons/(?P<id>\d+)/$', 'main.views.lesson_page_view', name='lessons'),
    url(r'^about/$', 'main.views.about_view', name='about'),
    url(r'^more/$', 'main.views.more_view', name='more'),
    url(r'^lessontest/(?P<lesson_id>\d+)/$', 'main.views.lesson_test', name='test_lesson'),
    url(r'^education/$', 'main.views.education_view', name='education'),
    url(r'^videolessons/$', 'main.views.video_lesson_view', name='videolessons'),
    url(r'^lesson/(?P<id>\d+)/$', 'main.views.single_lesson', name='single_lesson'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
