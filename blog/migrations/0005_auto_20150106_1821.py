# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150106_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='title',
        ),
    ]
