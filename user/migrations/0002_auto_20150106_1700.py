# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='user',
            field=models.OneToOneField(verbose_name='\u7528\u6237', to='user.User'),
            preserve_default=True,
        ),
    ]
