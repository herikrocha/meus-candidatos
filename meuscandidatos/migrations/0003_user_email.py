# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuscandidatos', '0002_auto_20171003_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='teste', max_length=254),
            preserve_default=False,
        ),
    ]
