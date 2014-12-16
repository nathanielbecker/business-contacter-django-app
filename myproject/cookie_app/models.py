from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib import admin
from datetime import datetime

##this is a hacky way to get inline forms--see http://lightbird.net/dbe/todo_list.html
class DateTime(models.Model):
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    def __unicode__(self):
        return unicode(self.datetime)
######################################

class Initial_Borr_List_Page(models.Model):
	BorrName = models.CharField(max_length=150, verbose_name = "Company Name", default='0000000')
	BorrStreet = models.CharField(max_length=150, verbose_name = "Address", default='0000000',blank=True)
	BorrState = models.CharField(max_length=150, verbose_name = "City", default='0000000',blank=True)
	BorrCity = models.CharField(max_length=150, verbose_name = "State", default='0000000',blank=True)
	BorrZip = models.CharField(max_length=150, verbose_name = "ZIP Code", default='0000000',blank=True)
	BorrCounty= models.CharField(max_length=150, verbose_name = "County", default='0000000',blank=True)
	BorrPhoneNumber= models.CharField(max_length=150, verbose_name = "Phone Number Combined", default='0000000',blank=True)
	BorrWebsite= models.CharField(max_length=150, verbose_name = "Website", default='0000000',blank=True)
	BorrEmployees= models.CharField(max_length=150, verbose_name = "Number Employee (est.)", default='0000000',blank=True)
	BorrSales= models.CharField(max_length=150, verbose_name = "Sales Volume (est.)", default='0000000',blank=True)
	BorrAge= models.CharField(max_length=150, verbose_name = "Years In Database", default='0000000',blank=True)
	BorrSICName= models.CharField(max_length=150, verbose_name = "Line of Business", default='0000000',blank=True)
	Created = models.ForeignKey(DateTime, null=True)
	FindMoreData = models.BooleanField(default=False, verbose_name = "Find More Information")
	def __str__(self):
		return self.BorrName
	def get_absolute_url(self):
		return reverse('Initial_Borr_List_Page_detail', args=[str(self.id)])


class More_Data_Page(models.Model):
	FollowUp=  models.BooleanField(default=False, verbose_name = "Contact Business")
	BorrName= models.ForeignKey(Initial_Borr_List_Page, null=True)
	BorrYelpLink= models.CharField(max_length=150, verbose_name = "Yelp link", default='0000000',blank=True)
	BorrYelpNumReviews= models.CharField(max_length=150, verbose_name = "Yelp # of reviews", default='0000000',blank=True)
	BorrFacebookPage= models.CharField(max_length=150, verbose_name = "Facebook page", default='0000000',blank=True)
	BorrPreviousLender= models.CharField(max_length=150, verbose_name = "Previous lender", default='0000000',blank=True)
	BorrLastLoanDate= models.CharField(max_length=150, verbose_name = "Last loan date", default='0000000',blank=True)
	BorrLastLoanMaturity= models.CharField(max_length=150, verbose_name = "Loan maturity date", default='0000000',blank=True)
	BorrLoanType= models.CharField(max_length=150, verbose_name = "Loan type", default='0000000',blank=True)
	BorrPhoneNumberVal= models.CharField(max_length=150, verbose_name = "Validated phone number", default='0000000',blank=True)
	BorrLoanProb= models.CharField(max_length=150, verbose_name = "Likelihood of getting a loan", default='0000000',blank=True)
	BorrEmail= models.CharField(max_length=150, verbose_name = "Validated email", default='0000000',blank=True)
	BorrWebsiteVal= models.CharField(max_length=150, verbose_name = "Validated website", default='0000000',blank=True)
	BorrSquareft= models.CharField(max_length=150, verbose_name = "Square footage", default='0000000',blank=True)
	BorrOwnRent= models.CharField(max_length=150, verbose_name = "Own or rent building", default='0000000',blank=True)
	def __str__(self):
		return self.BorrName
	def get_absolute_url(self):
		return reverse('More_Data_Page_detail', args=[str(self.id)])



# FollowUp = models.BooleanField(default=False, verbose_name = "Contact Business?")
