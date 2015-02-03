# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0021_auto_20150121_0043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='initial_borr_list_page',
            options={'verbose_name_plural': 'Initial Data'},
        ),
        migrations.AlterModelOptions(
            name='more_data_page',
            options={'verbose_name_plural': 'Followup Data'},
        ),
    ]
