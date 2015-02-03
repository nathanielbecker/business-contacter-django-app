# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0017_ox'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ox',
        ),
        migrations.AlterModelOptions(
            name='more_data_page',
            options={'verbose_name_plural': 'oxen'},
        ),
    ]
