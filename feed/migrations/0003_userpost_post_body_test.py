# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-10 01:05
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_userpost_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='post_body_test',
            field=ckeditor.fields.RichTextField(default='Text'),
        ),
    ]
