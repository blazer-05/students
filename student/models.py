# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=256, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='photo/student/%Y/%m/%d', blank=True, verbose_name='Фото')
    ticket = models.CharField(max_length=256, verbose_name='Билет')
    notes = models.TextField(blank=True, verbose_name='Особые отметки')

    class Meta:
        verbose_name = 'Студен'
        verbose_name_plural = 'Студенты'

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Group(models.Model):
    title = models.CharField(max_length=256, verbose_name='Имя')
    leader = models.OneToOneField('Student', blank=True, null=True, verbose_name='Староста', on_delete=models.SET_NULL)
    notes = models.TextField(blank=True, verbose_name='Заметки')
    student_group = models.ForeignKey('Group', verbose_name='Группа', null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __unicode__(self):
        if self.leader:
            return '%s (%s %s)' % (self.title, self.leader.first_name, self.leader.last_name)
        else:
            return '%s' % (self.title,)