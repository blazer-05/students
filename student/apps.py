# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class StudentConfig(AppConfig):
    name = 'student'

class StudentsAppConfig(AppConfig):
    name = 'student'
    verbose_name = u'База Студентов'

    def ready(self):
        from student import signals