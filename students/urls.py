# -*- coding: utf-8 -*-
"""students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from student.views.contact_admin import contact_admin
from student.views.students import student_list, student_add
from student.views.groups import groups_list, groups_add, groups_edit, groups_delete

from student.views.students import StudentUpdateView, StudentDeleteView
from student.views.journal import JournalView

urlpatterns = [
    url(r'^$', student_list, name='home'),
    url(r'^student/add/$', student_add, name='student_add'),
    url(r'^student/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='student_edit'),
    url(r'^student/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='student_delete'),

    url(r'^groups/$', groups_list, name='groups'),
    url(r'^groups/add/$', groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups_delete, name='groups_delete'),

    # Journal urls
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    url(r'^contact-admin/$', contact_admin, name='contact_admin'),
    url(r'^admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     if settings.MEDIA_ROOT:
#         urlpatterns += static(settings.MEDIA_URL,
#             document_root=settings.MEDIA_ROOT)