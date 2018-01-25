
from django.db import models

from django.utils.translation import ugettext_lazy as _

class MonthJournal(models.Model):
    student = models.ForeignKey('Student', verbose_name=_('Student'), blank=False, unique_for_month='date')
    date = models.DateField(verbose_name=_('Date'), blank=False)

    class Meta:
        verbose_name = _('Monthly Journal')
        verbose_name_plural = _('Monthly Journals')

    def __unicode__(self):
        return u'%s: %d %d' % (self.student.last_name, self.date.month, self.date.year)

for num in range(1, 32):
    MonthJournal.add_to_class('present_day'+str(num), models.BooleanField(default=False))