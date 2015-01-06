# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150106_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Category',
            new_name='category',
        ),
    ]
