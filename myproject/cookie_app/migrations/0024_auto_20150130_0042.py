# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_app', '0023_auto_20150129_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='Revenue_Yr',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Revenue (est.)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='Website',
            field=models.URLField(default='0000000', max_length=150, null=True, verbose_name='Website'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='X2013_Employees',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Employees (2013 est.)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='X2013_Revenue_Yr',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Revenue (2013 est.)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='centile',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Loan Likelihood Score'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='checkins',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Facebook Checkins'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='final_employees',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Employees (est.)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='final_phone',
            field=models.CharField(default='0000000', max_length=150, null=True, verbose_name='Phone Number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='final_yr_incorporated',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Year of Incorporation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='likes',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Facebook Likes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='link',
            field=models.URLField(default='0000000', max_length=150, null=True, verbose_name='Facebook Link'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='num_loans',
            field=models.IntegerField(default='0000000', null=True, verbose_name='SBA Loans (2007+)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='review_count',
            field=models.IntegerField(default='0000000', null=True, verbose_name='Yelp Review Count'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='sum_loans',
            field=models.IntegerField(default='0000000', null=True, verbose_name='SBA Loan vol. (2007+)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='initial_borr_list_page',
            name='url',
            field=models.URLField(default='0000000', max_length=150, null=True, verbose_name='Yelp Link'),
            preserve_default=True,
        ),
    ]
