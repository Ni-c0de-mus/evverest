# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-09 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_userprofile_user_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_level',
            field=models.IntegerField(default=1),
        ),
    ]
