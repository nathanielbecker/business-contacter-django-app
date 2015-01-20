# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0013_auto_20141215_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='more_data_page',
            name='BorrOwnerName',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Owner Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrEmail',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Validated email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrFacebookPage',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Facebook page'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrLastLoanDate',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Last loan date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrLastLoanMaturity',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Loan maturity date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrLoanProb',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Likelihood of getting a loan'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrLoanType',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Loan type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrOwnRent',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Own or rent building'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrPhoneNumberVal',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Validated phone number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrPreviousLender',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Previous lender'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrSquareft',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Square footage'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrWebsiteVal',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Validated website'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrYelpLink',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Yelp link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='more_data_page',
            name='BorrYelpNumReviews',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Yelp # of reviews'),
            preserve_default=True,
        ),
    ]
