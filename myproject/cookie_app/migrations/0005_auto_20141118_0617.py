# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0004_auto_20141118_0615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barebones_crud',
            old_name='concatname',
            new_name='name',
        ),
    ]
