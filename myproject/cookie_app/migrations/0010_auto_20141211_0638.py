# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0009_auto_20141211_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barebones_crud',
            name='FindMoreData',
            field=models.BooleanField(default=False, verbose_name='Find More Information on Business?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='FollowUp',
            field=models.BooleanField(default=False, verbose_name='Contact Business?'),
            preserve_default=True,
        ),
    ]
