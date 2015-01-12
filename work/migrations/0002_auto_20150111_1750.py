# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ForeignKey(verbose_name='\u4ea7\u54c1\u56fe\u7247', blank=True, to='work.ProductImage', null=True),
            preserve_default=True,
        ),
    ]
