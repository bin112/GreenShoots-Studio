# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(max_length=25, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('product_url', models.URLField(null=True, verbose_name='\u4ea7\u54c1\u94fe\u63a5', blank=True)),
                ('description', models.TextField(verbose_name='\u4ea7\u54c1\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1',
                'verbose_name_plural': '\u4ea7\u54c1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('name', models.CharField(max_length=20, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('image', models.ImageField(upload_to=b'/product', verbose_name='\u4ea7\u54c1\u56fe\u7247')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u56fe\u7247',
                'verbose_name_plural': '\u4ea7\u54c1\u56fe\u7247',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ForeignKey(verbose_name='\u4ea7\u54c1\u56fe\u7247', to='work.ProductImage'),
            preserve_default=True,
        ),
    ]
