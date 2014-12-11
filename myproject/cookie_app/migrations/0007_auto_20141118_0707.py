# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0006_auto_20141118_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='barebones_crud',
            name='FindMoreData',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='FollowUp',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
