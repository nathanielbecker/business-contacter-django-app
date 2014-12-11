# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0002_remove_barebones_crud_durr'),
    ]

    operations = [
        migrations.AddField(
            model_name='barebones_crud',
            name='durr',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
