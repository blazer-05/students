# -*- coding: UTF-8 -*-
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.translation import ugettext as _

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

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'leader', 'notes']

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # add form or edit form
        if kwargs['instance'] is None:
            add_form = True
        else:
            add_form = False

        # set form tag attributes
        if add_form:
            self.helper.form_action = reverse('groups_add')
        else:
            self.helper.form_action = reverse('groups_edit',
                kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # add buttons
        if add_form:
            submit = Submit('add_button', _(u"Add"),
                css_class="btn btn-primary")
        else:
            submit = Submit('save_button', _(u"Save"),
                css_class="btn btn-primary")
        self.helper.layout[-1] = FormActions(
            submit,
            Submit('cancel_button', _(u"Cancel"), css_class="btn btn-link"),
        )

class BaseGroupFormView(object):

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('groups'),
            _(u"Changes saved successfully!"))

    def post(self, request, *args, **kwargs):
        # handle cancel button
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('groups') +
                u'?status_message=%s' % _(u"Changes canceled."))
        else:
            return super(BaseGroupFormView, self).post(
                request, *args, **kwargs)

class GroupAddView(BaseGroupFormView, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'student/groups_form.html'

class GroupUpdateView(BaseGroupFormView, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'student/groups_form.html'

class GroupDeleteView(BaseGroupFormView, DeleteView):
    model = Group
    template_name = 'student/groups_confirm_delete.html'
