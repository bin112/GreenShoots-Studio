# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150106_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='hello', unique=True, max_length=200, verbose_name='\u94fe\u63a5\u540d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='hello', unique=True, max_length=200, verbose_name='\u94fe\u63a5\u540d'),
            preserve_default=False,
        ),
    ]
