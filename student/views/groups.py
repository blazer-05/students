# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def groups_list(request):
    groups = (
        {'id': 1,
         'name': 'МтМ-1',
         'leader': {'id': 1, 'name': 'Корост Андрей'}},
        {'id': 2,
         'name': 'МтМ-22',
         'leader': {'id': 2, 'name': ' Подоба Виталий'}},
        {'id': 3,
         'name': 'МтМ-23',
         'leader': {'id': 3, 'name': ' Притула Тарас'}},
        {'id': 4,
         'name': 'МтМ-24',
         'leader': {'id': 4, 'name': ' Иванов Иван'}},
        {'id': 5,
         'name': 'МтМ-25',
         'leader': {'id': 5, 'name': ' Петров Алексей'}},

    )
    return render(request, 'student/group_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
