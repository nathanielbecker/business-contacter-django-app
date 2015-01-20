# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0015_auto_20150105_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrLoanProb',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Loan Probability'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrOwnRent',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Own or rent'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrPhoneNumberVal',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Validated phone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrYelpNumReviews',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Yelp # reviews'),
            preserve_default=True,
        ),
    ]
