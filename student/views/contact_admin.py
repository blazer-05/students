# -*- coding: UTF-8 -*-
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.core.urlresolvers import reverse

class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Отправить'))

    from_email = forms.EmailField(label='Ваш e-mail')
    subject = forms.CharField(label='Заголовок письма', max_length=128)
    message = forms.CharField(label='Текст сообщения', max_length=2560, widget=forms.Textarea)
    copy = forms.BooleanField(required=False, label='Отправить копию себе')

def contact_admin(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            copy = form.cleaned_data['copy']
            recepients = ['blazer-05@mail.ru']

            if copy:
                recepients.append(from_email)
            try:
                send_mail(subject, message, 'blazer-05@mail.ru', recepients)
            except Exception:
                message = u'При отправке сообщения возникла непредвиденная ошибка. Попробуйте отправить еще раз.'
            else:
                message = u'Ваше сообщение успешно отправленно!'
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('contact_admin'), message))
    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})


'''
class ContactView(FormView):
    template_name = 'contact_admin/form.html'
    form_class = ContactForm
    success_url = '/email-sent/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
        send_mail(subject, message, from_email, ['atari1971@mail.ru'])
        return super(ContactView, self).form_valid(form)


def contact_admin(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, ['atari1971@mail.ru'])
            except Exception:
                message = u'При отправке сообщения возникла непредвиденная ошибка. Попробуйте отправить еще раз.'
            else:
                message = u'Ваше сообщение успешно отправленно!'
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('contact_admin'), message))
    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})
'''