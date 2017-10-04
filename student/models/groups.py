# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

class Group(models.Model):
    title = models.CharField(max_length=256, verbose_name='Имя')
    leader = models.OneToOneField('Student', blank=True, null=True, verbose_name='Староста', on_delete=models.SET_NULL)
    notes = models.TextField(blank=True, verbose_name='Заметки')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __unicode__(self):
        if self.leader:
            return '%s (%s %s)' % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return '%s' % (self.title,)