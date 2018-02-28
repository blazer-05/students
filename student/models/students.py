
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Student(models.Model):
    first_name = models.CharField(max_length=256, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=256, verbose_name=_('Last Name'))
    middle_name = models.CharField(max_length=256, verbose_name=_('Middle Name'))
    birthday = models.DateField(verbose_name=_('Birthday'))
    photo = models.ImageField(upload_to='photo/student/%Y/%m/%d', blank=True, verbose_name=_('Photo'))
    ticket = models.CharField(max_length=256, verbose_name=_('Ticket'))
    notes = models.TextField(blank=True, verbose_name=_('Extra Notes'))
    student_group = models.ForeignKey('Group', verbose_name=_('Group'), null=True, on_delete=models.PROTECT)


    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Privacy(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    privacy = models.TextField(blank=True, verbose_name='privacy')

    class Meta:
        verbose_name = 'Privacy'

    def __unicode__(self):
        return self.title
