# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def student_list(request):
    students = Student.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    paginator = Paginator(students, 3)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

    return render(request, 'student/students_list.html', {'students': students})

def student_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def student_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def student_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

'''
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
'''