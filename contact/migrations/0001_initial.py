# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(max_length=10, verbose_name='\u59d3\u540d')),
                ('phone', models.CharField(max_length=18, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('email', models.EmailField(max_length=75, verbose_name='\u90ae\u7bb1')),
                ('description', models.TextField(verbose_name='\u9700\u6c42\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u8054\u7cfb\u6211\u4eec',
                'verbose_name_plural': '\u8054\u7cfb\u6211\u4eec',
            },
            bases=(models.Model,),
        ),
    ]
