# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(max_length=25, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
                ('is_published', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53d1\u5e03')),
                ('click_count', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u91cf', editable=False)),
                ('comment_count', models.IntegerField(default=0, verbose_name='\u8bc4\u8bba\u6570', editable=False)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '\u535a\u5ba2',
                'verbose_name_plural': '\u535a\u5ba2',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('count', models.IntegerField(default=0, verbose_name='\u5f15\u7528\u6b21\u6570')),
            ],
            options={
                'db_table': 'blog_theme',
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('count', models.IntegerField(default=0, verbose_name='\u5f15\u7528\u6b21\u6570')),
            ],
            options={
                'db_table': 'blog_tag',
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='Category',
            field=models.ForeignKey(verbose_name='\u4e3b\u9898', blank=True, to='blog.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(verbose_name='\u4f5c\u8005', to='user.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', null=True, verbose_name='\u6807\u7b7e', blank=True),
            preserve_default=True,
        ),
    ]
