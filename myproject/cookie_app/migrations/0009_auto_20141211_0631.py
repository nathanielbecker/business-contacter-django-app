# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0008_auto_20141120_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barebones_crud',
            name='FollowUp',
            field=models.BooleanField(default=False, verbose_name='pizzafff'),
            preserve_default=True,
        ),
    ]
