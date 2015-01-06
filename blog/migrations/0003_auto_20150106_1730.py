# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to=b'blog', null=True, verbose_name='\u9898\u56fe', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(unique=True, max_length=200, verbose_name='\u94fe\u63a5\u540d'),
            preserve_default=True,
        ),
    ]
