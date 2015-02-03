# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0024_auto_20150130_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='final_phone',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Validated Phone'),
            preserve_default=True,
        ),
    ]
