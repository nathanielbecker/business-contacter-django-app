# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0003_barebones_crud_durr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barebones_crud',
            name='created',
        ),
        migrations.RemoveField(
            model_name='barebones_crud',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='barebones_crud',
            name='done',
        ),
        migrations.RemoveField(
            model_name='barebones_crud',
            name='durr',
        ),
        migrations.RemoveField(
            model_name='barebones_crud',
            name='name',
        ),
        migrations.RemoveField(
            model_name='barebones_crud',
            name='priority',
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrCity',
            field=models.CharField(default='0000000', max_length=150),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrName',
            field=models.CharField(default='0000000', max_length=150),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrState',
            field=models.CharField(default='0000000', max_length=150),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrStreet',
            field=models.CharField(default='0000000', max_length=150),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrZip',
            field=models.CharField(default='0000000', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='concatname',
            field=models.CharField(default='0000000', max_length=150),
            preserve_default=True,
        ),
    ]
