# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20150111_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=DjangoUeditor.models.UEditorField(null=True, verbose_name='\u4ea7\u54c1\u63cf\u8ff0', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=b'product', verbose_name='\u4ea7\u54c1\u56fe\u7247'),
            preserve_default=True,
        ),
    ]
