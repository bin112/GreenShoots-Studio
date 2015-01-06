# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150106_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='qq',
            field=models.CharField(max_length=15, verbose_name='qq\u8d26\u53f7', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='signature',
            field=models.CharField(max_length=300, verbose_name='\u4e2a\u6027\u7b7e\u540d', blank=True),
            preserve_default=True,
        ),
    ]
