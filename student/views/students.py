# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView
from django.utils.translation import ugettext as _

from student.models import Student, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..util import paginate, get_current_group

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions


# Вывод всего списка студентов на страницу
def student_list(request):
    # check if we need to show only one group of students
    current_group = get_current_group(request)
    if current_group:
        students = Student.objects.filter(student_group=current_group)
    else:
        # otherwise show all students
        students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # apply pagination, 3 students per page
    context = paginate(students, 3, request, {}, var_name='students')

    return render(request, 'student/students_list.html', context)

# Добавление студента
def student_add(request):
    if request.method == 'POST':
        if request.POST.get('add_button') is not None:
            errors = {}
            data = {'middle_name': request.POST.get('middle_name'), 'notes': request.POST.get('notes')}

            first_name=request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = _('First Name field is required')
            else:
                data['first_name'] = first_name

            last_name=request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = _('Last Name field is required')
            else:
                data['last_name'] = last_name

            birthday=request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = _('This field is required.')
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = _('Enter the correct date format')
                else:
                    data['birthday'] = birthday

            ticket=request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = _('Ticket number is a required field')
            else:
                data['ticket'] = ticket

            student_group=request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = _('Select a group for the student')
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = _('Select the correct group')
                else:
                    data['student_group'] = groups[0]

            photo=request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            if not errors:
                student = Student(**data)
                student.save()
                return HttpResponseRedirect(
                    u'%s?status_message=%s' % (reverse('home')), _('The student was successfully added!'))
            else:
                return render(request, 'student/students_add.html', {'groups': Group.objects.all().order_by('title'),
                                                                     'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('home'), _('Student additions canceled!')))
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
            Submit('add_button', _(u'Save'), css_class='btn btn-primary'),
            Submit('cancel_button', _(u'Cancel'), css_class='btn btn-link'),
        )

# Редактирование студента и применения стилизации crispy-forms с помощью определенного класса StudentUpdateForm
class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/students_edit.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('home')), _('The student was successfully saved!')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('home')), _('Editing of the student is canceled!'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

# Удаление студента
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/students_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('home')), _('Student successfully deleted!')


from django.utils.translation import ugettext as _
def test(request):
    return render(request, 'student/test.html', {'message': _("It's a good weather today!") })


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