# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0005_auto_20141118_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrCity',
            field=models.CharField(default='0000004', max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrName',
            field=models.CharField(default='0000001', max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrState',
            field=models.CharField(default='0000003', max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrStreet',
            field=models.CharField(default='0000002', max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrZip',
            field=models.CharField(default='0000005', max_length=15),
            preserve_default=True,
        ),
    ]
