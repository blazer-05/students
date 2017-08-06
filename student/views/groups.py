# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from ..models import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def groups_list(request):
    groups = Group.objects.all()
    order_by = request.GET.get('order_by', '')
    if order_by in ('title',):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    paginator = Paginator(groups, 1)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        groups = paginator.page(paginator.num_pages)
    return render(request, 'student/group_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
