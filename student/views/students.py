# -*- coding: UTF-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView

from student.models import Student, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

# Вывод всего списка студентов на страницу
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

# Добавление студента
def student_add(request):
    if request.method == 'POST':
        if request.POST.get('add_button') is not None:
            errors = {}
            data = {'middle_name': request.POST.get('middle_name'), 'notes': request.POST.get('notes')}

            first_name=request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = 'Имя это обязательное поле'
            else:
                data['first_name'] = first_name

            last_name=request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = 'Фамилия это обязательное поле'
            else:
                data['last_name'] = last_name

            birthday=request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = 'Это обязательное поле к заполнению'
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = 'Введите корректных формат даты'
                else:
                    data['birthday'] = birthday

            ticket=request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = 'Номер билета это обязательное поле'
            else:
                data['ticket'] = ticket

            student_group=request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = 'Выберите группу для студента'
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = 'Выберите корректную группу'
                else:
                    data['student_group'] = groups[0]

            photo=request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            if not errors:
                student = Student(**data)
                student.save()
                return HttpResponseRedirect(
                    u'%s?status_message=Студент успешно добавлен!' % reverse('home'))
            else:
                return render(request, 'student/students_add.html', {'groups': Group.objects.all().order_by('title'),
                                                                     'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(
                u'%s?status_message=Добавление студента отменено!' % reverse('home'))
    else:
        return render(request, 'student/students_add.html', {'groups': Group.objects.all().order_by('title')})

# Определение класса для стилизации формы редактирования студента (django-crispy-forms)
class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        # set form tag attributes
        try:
            self.helper.form_action = reverse('student_edit', kwargs={'pk': kwargs['instanse'].id})
        except:
            self.helper.form_action = reverse('home')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        self.helper.layout[-1] = FormActions(
            Submit('add_button', u'Сохранить', css_class='btn btn-primary'),
            Submit('cancel_button', u'Отменить', css_class='btn btn-link'),
        )

# Редактирование студента и применения стилизации crispy-forms с помощью определенного класса StudentUpdateForm
class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        return u'%s?status_message=Студент успешно сохранен!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редактирование студента отменено!' % reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

# Удаление студента
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/students_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=Студента успішно видалено!' % reverse('home')

'''

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/students_edit.html'

    def get_success_url(self):
        return u'%s?status_message=Студент успешно сохранен!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редактирование студента отменено!' % reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

def student_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def student_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

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