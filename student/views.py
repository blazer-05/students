# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def student_list(request):
    return render(request, 'student/students_list.html', {})

def student_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def student_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def student_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
    return HttpResponse('<h1>Group add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)


