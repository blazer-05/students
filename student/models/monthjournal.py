# -*- coding: UTF-8 -*-
from django.db import models

class MonthJournal(models.Model):
    student = models.ForeignKey('Student', verbose_name='Студент', blank=False, unique_for_month='date')
    date = models.DateField(verbose_name='Дата', blank=False)

    class Meta:
        verbose_name = 'Месячный журнал'
        verbose_name_plural = 'Месячные журналы'

    def __unicode__(self):
        return u'%s: %d %d' % (self.student.last_name, self.date.month, self.date.year)

for num in range(1, 32):
    MonthJournal.add_to_class('present_day'+str(num), models.BooleanField(default=False))