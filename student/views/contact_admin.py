
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

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
        self.helper.add_input(Submit('send_button', _(u'Send')))

    from_email = forms.EmailField(label=_(u'You E-mail'))
    subject = forms.CharField(label=_(u'Name of the letter'), max_length=128)
    message = forms.CharField(label=_(u'Text message'), max_length=2560, widget=forms.Textarea)
    copy = forms.BooleanField(required=False, label=_(u'Send a copy to myself'))

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
                message = _(u'An unexpected error occurred while sending the message. Please try to send again.')
            else:
                message = _(u'Your message was successfully sent!')
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('contact_admin'), message))
    else:
        form = ContactForm()
    return render(request, 'contact_admin/form.html', {'form': form})
