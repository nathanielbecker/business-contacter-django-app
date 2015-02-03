# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0018_auto_20150121_0037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='more_data_page',
            options={'verbose_name': 'Followup Data'},
        ),
    ]
