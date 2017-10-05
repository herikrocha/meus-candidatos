# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 03:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuscandidatos', '0010_auto_20171005_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskills',
            name='androidDevelopment',
            field=models.PositiveIntegerField(blank=True, error_messages={'max_value': 'O valor deve estar entre 0 e 10'}, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='userskills',
            name='css',
            field=models.PositiveIntegerField(blank=True, error_messages={'max_value': 'O valor deve estar entre 0 e 10'}, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='userskills',
            name='django',
            field=models.PositiveIntegerField(blank=True, error_messages={'max_value': 'O valor deve estar entre 0 e 10'}, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='userskills',
            name='html',
            field=models.PositiveIntegerField(blank=True, error_messages={'max_value': 'O valor deve estar entre 0 e 10'}, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='userskills',
            name='iosDevelopment',
            field=models.PositiveIntegerField(blank=True, error_messages={'max_value': 'O valor deve estar entre 0 e 10'}, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='userskills',
            name='javascript',
            field=models.PositiveIntegerField(blank=True, error_messages={'max_value': 'O valor deve estar entre 0 e 10'}, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='userskills',
            name='python',
            field=models.PositiveIntegerField(blank=True, error_messages={'max_value': 'O valor deve estar entre 0 e 10'}, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
