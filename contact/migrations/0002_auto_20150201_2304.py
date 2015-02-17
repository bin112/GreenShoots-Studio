# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(null=True, verbose_name='\u9700\u6c42\u63cf\u8ff0', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=75, null=True, verbose_name='\u90ae\u7bb1', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=10, null=True, verbose_name='\u59d3\u540d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=18, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd', blank=True),
            preserve_default=True,
        ),
    ]
