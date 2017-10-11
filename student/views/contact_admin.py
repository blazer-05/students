# -*- coding: UTF-8 -*-
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.core.urlresolvers import reverse

from students.settings import ADMIN_EMAIL


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Ваш e-mail')
    subject = forms.CharField(label='Заголовок письма', max_length=128)
    message = forms.CharField(label='Текст сообщения', max_length=2560, widget=forms.Textarea)


def contact_admin(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = 'При отправке сообщения возникла непредвиденная ошибка. Попробуйте отправить еще раз.'
            else:
                message = 'Ваше сообщение успешно отправленно!'
            return HttpResponseRedirect('%s?status_message%s' % (reverse('contact_admin')), message)
    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})