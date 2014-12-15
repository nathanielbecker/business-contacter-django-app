# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0011_auto_20141213_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrAge',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Years In Database', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrCity',
            field=models.CharField(default='0000000', max_length=150, verbose_name='State', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrCounty',
            field=models.CharField(default='0000000', max_length=150, verbose_name='County', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrEmployees',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Number Employee (est.)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrPhoneNumber',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Phone Number Combined', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrSICName',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Line of Business', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrSales',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Sales Volume (est.)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrState',
            field=models.CharField(default='0000000', max_length=150, verbose_name='City', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrStreet',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Address', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrWebsite',
            field=models.CharField(default='0000000', max_length=150, verbose_name='Website', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='barebones_crud',
            name='BorrZip',
            field=models.CharField(default='0000000', max_length=150, verbose_name='ZIP Code', blank=True),
            preserve_default=True,
        ),
    ]
