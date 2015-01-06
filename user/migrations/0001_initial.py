# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basicinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('nickname', models.CharField(max_length=30, verbose_name='\u6635\u79f0')),
                ('avatar', models.ImageField(upload_to=b'user/basicinfo', verbose_name='\u5934\u50cf')),
                ('sex', models.CharField(blank=True, max_length=1, verbose_name='\u6027\u522b', choices=[(b'M', '\u7537'), (b'F', '\u5973')])),
                ('email', models.EmailField(max_length=75, verbose_name='\u90ae\u7bb1', blank=True)),
                ('qq', models.CharField(max_length=15, verbose_name='qq\u8d26\u53f7')),
                ('signature', models.CharField(max_length=300, verbose_name='\u4e2a\u6027\u7b7e\u540d')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u8d44\u6599',
                'verbose_name_plural': '\u7528\u6237\u8d44\u6599',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(unique=True, max_length=25, verbose_name='\u59d3\u540d', db_index=True)),
                ('password', models.CharField(default=b'', max_length=128, verbose_name='\u5bc6\u7801')),
                ('status', models.CharField(max_length=1, verbose_name='\u7528\u6237\u72b6\u6001', choices=[(b'S', '\u542f\u7528'), (b'F', '\u7981\u7528')])),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='basicinfo',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237', to='user.User'),
            preserve_default=True,
        ),
    ]
