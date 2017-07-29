# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def student_list(request):
    students = (
        {'id': 1,
         'first_name': 'Андрей',
         'last_name': 'Корост',
         'ticket': 2123,
         'image': 'student/img/python.png'
         },
        {'id': 2,
         'first_name': 'Виталий',
         'last_name': 'Подоба',
         'ticket': 254,
         'image': 'student/img/django-icon.png'
         },
        {'id': 3,
         'first_name': 'Тарас',
         'last_name': 'Притула',
         'ticket': 5332,
         'image': 'student/img/logo_youtube2.png'
         },
        {'id': 4,
         'first_name': 'Иван',
         'last_name': 'Иванов',
         'ticket': 4569,
         'image': 'student/img/pole-oblaka-nebo-windows.jpg'
         },
        {'id': 5,
         'first_name': 'Алексей',
         'last_name': 'Петров',
         'ticket': 8041,
         'image': 'student/img/buddha-temple-hd-wallpapers.jpg'
         },
    )
    return render(request, 'student/students_list.html', {'students': students})

def student_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def student_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def student_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

