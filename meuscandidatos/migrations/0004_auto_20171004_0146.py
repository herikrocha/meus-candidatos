# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 04:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meuscandidatos', '0003_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firstName',
            new_name='fullName',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastName',
        ),
    ]
