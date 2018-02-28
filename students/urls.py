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
from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from student.views.contact_admin import contact_admin
from student.views.students import student_list, student_add
from student.views.groups import GroupAddView, GroupUpdateView, GroupDeleteView, groups_list

from student.views.students import StudentUpdateView, StudentDeleteView, test, privacy
from student.views.journal import JournalView
from students.languages import lang

from django.views.i18n import javascript_catalog
#from django.conf.urls.i18n import i18n_patterns

from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView, TemplateView

from django.contrib.auth.decorators import login_required, permission_required

js_info_dict = {
    'packages': ('student', ),
}


urlpatterns = [
    url(r'^$', student_list, name='home'),
    url(r'^student/add/$', student_add, name='student_add'),
    url(r'^student/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='student_edit'),
    url(r'^student/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='student_delete'),

    # Groups urls
    url(r'^groups/$', login_required(groups_list), name='groups'),
    url(r'^groups/add/$', login_required(GroupAddView.as_view()), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', login_required(GroupUpdateView.as_view()), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', login_required(GroupDeleteView.as_view()), name='groups_delete'),

    # Journal urls
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    url(r'^contact-admin/$', contact_admin, name='contact_admin'),
    url(r'^admin/', admin.site.urls),
    url(r'^test/', login_required(test), name='test'),
    url(r'^privacy/', privacy, name='privacy'),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18\.js$', javascript_catalog, js_info_dict, name='js_translite'),
    url(r'^lang/(?P<lang_code>[a-z]{2})/$', lang, name='lang'),

    # User Related urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls', namespace='users')),

    url('', include('social_django.urls', namespace='social'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     if settings.MEDIA_ROOT:
#         urlpatterns += static(settings.MEDIA_URL,
#             document_root=settings.MEDIA_ROOT)