# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0026_auto_20150130_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='initial_borr_list_page',
            name='FollowUp',
            field=models.BooleanField(default=False, verbose_name='Contact Business'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='FindMoreData',
            field=models.BooleanField(default=False, verbose_name='Find More Information'),
            preserve_default=True,
        ),
    ]
