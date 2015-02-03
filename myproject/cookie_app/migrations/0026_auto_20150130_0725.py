# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0025_auto_20150130_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrEmail',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrFacebookPage',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrLastLoanDate',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrLastLoanMaturity',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrLoanProb',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrLoanType',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrName',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrOwnRent',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrOwnerName',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrPhoneNumberVal',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrPreviousLender',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrSquareft',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrWebsiteVal',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrYelpLink',
        ),
        migrations.RemoveField(
            model_name='more_data_page',
            name='BorrYelpNumReviews',
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='AtoZ_ID',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='id'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='BankName',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Lender Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='Business_Name',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Company Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='Est_Rent_Annual_Expense',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Estimated Rent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='Franchise',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Franchise'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='InitialInterestRate',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Interest Rate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='Main_Line_of_Business',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Industry'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='Manufacturer',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Manufacturer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='NaicsDescription',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='NAICS Description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='Physical_City',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='City'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='Physical_State',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='Physical_ZIP',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Zip'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='Revenue_Yr',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Revenue (est.)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='Square_Footage',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Square Footage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='Website',
            field=models.URLField(default='0000000', max_length=150, null=True, verbose_name='Website'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='X2013_Employees',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Employees (2013 est.)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='X2013_Revenue_Yr',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Revenue (2013 est.)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='centile',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Loan Likelihood Score'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='checkins',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Facebook Checkins'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='executivedetails',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Executive Name'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='final_employees',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Employees (est.)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='final_phone',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Validated Phone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='final_yr_incorporated',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Year of Incorporation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='first_loan_date',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='First Loan Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='last_loan_date',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Last Loan Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='last_loan_end',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Last Loan End'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='likes',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Facebook Likes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='link',
            field=models.URLField(default='0000000', max_length=150, null=True, verbose_name='Facebook Link'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='num_loans',
            field=models.IntegerField(default='0000000', null=True, verbose_name='SBA Loans (2007+)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='ownsrentsindicator',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Own/Rent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='rating',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Yelp Rating'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='review_count',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Yelp Review Count'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='street3',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='sum_loans',
            field=models.IntegerField(default='0000000', null=True, verbose_name='SBA Loan vol. (2007+)'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='more_data_page',
            name='url',
            field=models.URLField(default='0000000', max_length=150, null=True, verbose_name='Yelp Link'),
            preserve_default=True,
        ),
    ]
