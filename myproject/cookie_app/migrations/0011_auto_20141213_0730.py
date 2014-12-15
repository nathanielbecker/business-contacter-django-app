# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0010_auto_20141211_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barebones_crud',
            name='FollowUp',
        ),
        migrations.RemoveField(
            model_name='barebones_crud',
            name='name',
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrAge',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Years In Database'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrCounty',
            field=models.CharField(default='0000000', max_length=150, verbose_name='County'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrEmployees',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Number Employee (est.)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrPhoneNumber',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Phone Number Combined'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrSICName',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Line of Business'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrSales',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Sales Volume (est.)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barebones_crud',
            name='BorrWebsite',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Website'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrCity',
            field=models.CharField(default='0000000', max_length=150, verbose_name='State'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrName',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Company Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrState',
            field=models.CharField(default='0000000', max_length=150, verbose_name='City'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrStreet',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrZip',
            field=models.CharField(default='0000000', max_length=150, verbose_name='ZIP Code'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='FindMoreData',
            field=models.BooleanField(default=False, verbose_name='Find More Information'),
            preserve_default=True,
        ),
    ]
