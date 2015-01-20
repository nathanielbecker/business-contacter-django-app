# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0014_auto_20150105_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='more_data_page',
            name='Created',
            field=models.ForeignKey(to='cookie_app.DateTime', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrName',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Company Name'),
            preserve_default=True,
        ),
    ]
