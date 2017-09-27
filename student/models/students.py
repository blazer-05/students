# -*- coding: UTF-8 -*-

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