# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0012_auto_20141213_0735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Initial_Borr_List_Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('BorrName', models.CharField(default='0000000', max_length=150, verbose_name='Company Name')),
                ('BorrStreet', models.CharField(default='0000000', max_length=150, verbose_name='Address', blank=True)),
                ('BorrState', models.CharField(default='0000000', max_length=150, verbose_name='City', blank=True)),
                ('BorrCity', models.CharField(default='0000000', max_length=150, verbose_name='State', blank=True)),
                ('BorrZip', models.CharField(default='0000000', max_length=150, verbose_name='ZIP Code', blank=True)),
                ('BorrCounty', models.CharField(default='0000000', max_length=150, verbose_name='County', blank=True)),
                ('BorrPhoneNumber', models.CharField(default='0000000', max_length=150, verbose_name='Phone Number Combined', blank=True)),
                ('BorrWebsite', models.CharField(default='0000000', max_length=150, verbose_name='Website', blank=True)),
                ('BorrEmployees', models.CharField(default='0000000', max_length=150, verbose_name='Number Employee (est.)', blank=True)),
                ('BorrSales', models.CharField(default='0000000', max_length=150, verbose_name='Sales Volume (est.)', blank=True)),
                ('BorrAge', models.CharField(default='0000000', max_length=150, verbose_name='Years In Database', blank=True)),
                ('BorrSICName', models.CharField(default='0000000', max_length=150, verbose_name='Line of Business', blank=True)),
                ('FindMoreData', models.BooleanField(default=False, verbose_name='Find More Information')),
                ('Created', models.ForeignKey(to='cookie_app.DateTime', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='More_Data_Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FollowUp', models.BooleanField(default=False, verbose_name='Contact Business')),
                ('BorrYelpLink', models.CharField(default='0000000', max_length=150, verbose_name='Yelp link', blank=True)),
                ('BorrYelpNumReviews', models.CharField(default='0000000', max_length=150, verbose_name='Yelp # of reviews', blank=True)),
                ('BorrFacebookPage', models.CharField(default='0000000', max_length=150, verbose_name='Facebook page', blank=True)),
                ('BorrPreviousLender', models.CharField(default='0000000', max_length=150, verbose_name='Previous lender', blank=True)),
                ('BorrLastLoanDate', models.CharField(default='0000000', max_length=150, verbose_name='Last loan date', blank=True)),
                ('BorrLastLoanMaturity', models.CharField(default='0000000', max_length=150, verbose_name='Loan maturity date', blank=True)),
                ('BorrLoanType', models.CharField(default='0000000', max_length=150, verbose_name='Loan type', blank=True)),
                ('BorrPhoneNumberVal', models.CharField(default='0000000', max_length=150, verbose_name='Validated phone number', blank=True)),
                ('BorrLoanProb', models.CharField(default='0000000', max_length=150, verbose_name='Likelihood of getting a loan', blank=True)),
                ('BorrEmail', models.CharField(default='0000000', max_length=150, verbose_name='Validated email', blank=True)),
                ('BorrWebsiteVal', models.CharField(default='0000000', max_length=150, verbose_name='Validated website', blank=True)),
                ('BorrSquareft', models.CharField(default='0000000', max_length=150, verbose_name='Square footage', blank=True)),
                ('BorrOwnRent', models.CharField(default='0000000', max_length=150, verbose_name='Own or rent building', blank=True)),
                ('BorrName', models.ForeignKey(to='cookie_app.Initial_Borr_List_Page', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='barebones_crud',
            name='Created',
        ),
        migrations.DeleteModel(
            name='barebones_CRUD',
        ),
    ]
