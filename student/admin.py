# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.forms import ModelForm, ValidationError

from .models import Student, Group, MonthJournal, Privacy
from django.core.urlresolvers import reverse

class StudentFormAdmin(ModelForm):

    def clean_student_group(self):
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(u'Студент является старастой другой группы.', code='invalid')
        return self.cleaned_data['student_group']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['-last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']
    form = StudentFormAdmin

    def view_on_site(self, obj):
        return reverse('student_edit', kwargs = {'pk': obj.id})

admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
admin.site.register(MonthJournal)
admin.site.register(Privacy)