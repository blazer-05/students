# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-20 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20180120_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthjournal',
            options={'verbose_name': 'Monthly Journal', 'verbose_name_plural': 'Monthly Journals'},
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student', unique_for_month=b'date', verbose_name='Student'),
        ),
    ]