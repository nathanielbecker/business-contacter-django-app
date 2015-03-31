from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib import admin
from datetime import datetime
from simple_history.models import HistoricalRecords # https://django-simple-history.readthedocs.org/en/latest/usage.html
# import versioning # from https://pypi.python.org/pypi/django-versioning

##this is a hacky way to get inline forms--see http://lightbird.net/dbe/todo_list.html
class DateTime(models.Model):
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    def __unicode__(self):
        return unicode(self.datetime)
######################################

class Initial_Borr_List_Page(models.Model):
    AtoZ_ID = models.CharField(max_length=150, verbose_name = "id", default='0000000',null=True)
    BankName = models.CharField(max_length=150, verbose_name = "Lender Name", default='0000000',null=True)
    Business_Name = models.CharField(max_length=150, verbose_name = "Company Name", default='0000000',null=True)
    checkins = models.CharField(max_length=150, verbose_name = "Facebook Checkins", default='0000000',null=True)
    Est_Rent_Annual_Expense = models.CharField(max_length=150, verbose_name = "Estimated Rent", default='0000000',null=True)
    executivedetails = models.CharField(max_length=150, verbose_name = "Executive Name", default='0000000',null=True)
    final_phone = models.CharField(max_length=150, verbose_name = "Validated Phone", default='0000000',null=True)
    first_loan_date = models.CharField(max_length=150, verbose_name = "First Loan Date", default='0000000',null=True)
    Franchise = models.CharField(max_length=150, verbose_name = "Franchise", default='0000000',null=True)
    InitialInterestRate = models.CharField(max_length=150, verbose_name = "Interest Rate", default='0000000',null=True)
    last_loan_date = models.CharField(max_length=150, verbose_name = "Last Loan Date", default='0000000',null=True)
    last_loan_end = models.CharField(max_length=150, verbose_name = "Last Loan End", default='0000000',null=True)
    likes = models.CharField(max_length=150, verbose_name = "Facebook Likes", default='0000000',null=True)
    link = models.URLField(max_length=150, verbose_name = "Facebook Link", default='0000000',null=True)
    final_employees = models.CharField(max_length=150, verbose_name = "Employees (est.)", default='0000000',null=True)
    Main_Line_of_Business = models.CharField(max_length=150, verbose_name = "Industry", default='0000000',null=True)
    Manufacturer = models.CharField(max_length=150, verbose_name = "Manufacturer", default='0000000',null=True)
    NaicsDescription = models.CharField(max_length=150, verbose_name = "NAICS Description", default='0000000',null=True)
    num_loans = models.CharField(max_length=150, verbose_name = "SBA Loans (2007+)", default='0000000',null=True)
    ownsrentsindicator = models.CharField(max_length=150, verbose_name = "Own/Rent", default='0000000',null=True)
    Physical_City = models.CharField(max_length=150, verbose_name = "City", default='0000000',null=True)
    Physical_State = models.CharField(max_length=150, verbose_name = "State", default='0000000',null=True)
    Physical_ZIP = models.CharField(max_length=150, verbose_name = "Zip", default='0000000',null=True)
    rating = models.CharField(max_length=150, verbose_name = "Yelp Rating", default='0000000',null=True)
    Revenue_Yr = models.CharField(max_length=150, verbose_name = "Revenue (est.)", default='0000000',null=True)
    review_count = models.CharField(max_length=150, verbose_name = "Yelp Review Count", default='0000000',null=True)
    Square_Footage = models.CharField(max_length=150, verbose_name = "Square Footage", default='0000000',null=True)
    street3 = models.CharField(max_length=150, verbose_name = "Address", default='0000000',null=True)
    sum_loans = models.CharField(max_length=150, verbose_name = "SBA Loan vol. (2007+)", default='0000000',null=True)
    Website = models.URLField(max_length=150, verbose_name = "Website", default='0000000',null=True)
    X2013_Employees = models.CharField(max_length=150, verbose_name = "Employees (2013 est.)", default='0000000',null=True)
    X2013_Revenue_Yr = models.CharField(max_length=150, verbose_name = "Revenue (2013 est.)", default='0000000',null=True)
    final_yr_incorporated = models.CharField(max_length=150, verbose_name = "Year of Incorporation", default='0000000',null=True)
    url = models.URLField(max_length=150, verbose_name = "Yelp Link", default='0000000',null=True)
    centile = models.CharField(max_length=150, verbose_name = "Loan Likelihood Score", default='0000000',null=True)
    Created = models.ForeignKey(DateTime, null=True)
    FindMoreData = models.BooleanField(default=False, verbose_name = "Find More Information")
    FollowUp=  models.BooleanField(default=False, verbose_name = "Contact Business")
    history = HistoricalRecords()
    def __str__(self):
        return self.BorrName
    def get_absolute_url(self):
        return reverse('Initial_Borr_List_Page_detail', args=[str(self.id)])
    class Meta:
        verbose_name_plural = "Initial Data"##to make navigation up top have real words


class More_Data_Page(models.Model):
    FindMoreData = models.BooleanField(default=False, verbose_name = "Find More Information")
    FollowUp=  models.BooleanField(default=False, verbose_name = "Contact Business")
    AtoZ_ID = models.CharField(max_length=150, verbose_name = "id", default='0000000',null=True)
    BankName = models.CharField(max_length=150, verbose_name = "Lender Name", default='0000000',null=True)
    Business_Name = models.CharField(max_length=150, verbose_name = "Company Name", default='0000000',null=True)
    checkins = models.CharField(max_length=150, verbose_name = "Facebook Checkins", default='0000000',null=True)
    Est_Rent_Annual_Expense = models.CharField(max_length=150, verbose_name = "Estimated Rent", default='0000000',null=True)
    executivedetails = models.CharField(max_length=150, verbose_name = "Executive Name", default='0000000',null=True)
    final_phone = models.CharField(max_length=150, verbose_name = "Validated Phone", default='0000000',null=True)
    first_loan_date = models.CharField(max_length=150, verbose_name = "First Loan Date", default='0000000',null=True)
    Franchise = models.CharField(max_length=150, verbose_name = "Franchise", default='0000000',null=True)
    InitialInterestRate = models.CharField(max_length=150, verbose_name = "Interest Rate", default='0000000',null=True)
    last_loan_date = models.CharField(max_length=150, verbose_name = "Last Loan Date", default='0000000',null=True)
    last_loan_end = models.CharField(max_length=150, verbose_name = "Last Loan End", default='0000000',null=True)
    likes = models.CharField(max_length=150, verbose_name = "Facebook Likes", default='0000000',null=True)
    link = models.URLField(max_length=150, verbose_name = "Facebook Link", default='0000000',null=True)
    final_employees = models.CharField(max_length=150, verbose_name = "Employees (est.)", default='0000000',null=True)
    Main_Line_of_Business = models.CharField(max_length=150, verbose_name = "Industry", default='0000000',null=True)
    Manufacturer = models.CharField(max_length=150, verbose_name = "Manufacturer", default='0000000',null=True)
    NaicsDescription = models.CharField(max_length=150, verbose_name = "NAICS Description", default='0000000',null=True)
    num_loans = models.CharField(max_length=150, verbose_name = "SBA Loans (2007+)", default='0000000',null=True)
    ownsrentsindicator = models.CharField(max_length=150, verbose_name = "Own/Rent", default='0000000',null=True)
    Physical_City = models.CharField(max_length=150, verbose_name = "City", default='0000000',null=True)
    Physical_State = models.CharField(max_length=150, verbose_name = "State", default='0000000',null=True)
    Physical_ZIP = models.CharField(max_length=150, verbose_name = "Zip", default='0000000',null=True)
    rating = models.CharField(max_length=150, verbose_name = "Yelp Rating", default='0000000',null=True)
    Revenue_Yr = models.CharField(max_length=150, verbose_name = "Revenue (est.)", default='0000000',null=True)
    review_count = models.CharField(max_length=150, verbose_name = "Yelp Review Count", default='0000000',null=True)
    Square_Footage = models.CharField(max_length=150, verbose_name = "Square Footage", default='0000000',null=True)
    street3 = models.CharField(max_length=150, verbose_name = "Address", default='0000000',null=True)
    sum_loans = models.CharField(max_length=150, verbose_name = "SBA Loan vol. (2007+)", default='0000000',null=True)
    Website = models.URLField(max_length=150, verbose_name = "Website", default='0000000',null=True)
    X2013_Employees = models.CharField(max_length=150, verbose_name = "Employees (2013 est.)", default='0000000',null=True)
    X2013_Revenue_Yr = models.CharField(max_length=150, verbose_name = "Revenue (2013 est.)", default='0000000',null=True)
    final_yr_incorporated = models.CharField(max_length=150, verbose_name = "Year of Incorporation", default='0000000',null=True)
    url = models.URLField(max_length=150, verbose_name = "Yelp Link", default='0000000',null=True)
    centile = models.CharField(max_length=150, verbose_name = "Loan Likelihood Score", default='0000000',null=True)
    Created = models.ForeignKey(DateTime, null=True)
    history = HistoricalRecords()
    @property # from https://django-simple-history.readthedocs.org/en/latest/advanced.html
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    def __str__(self):
        return self.BorrName
    def get_absolute_url(self):
        return reverse('More_Data_Page_detail', args=[str(self.id)])
    class Meta:
        verbose_name_plural = "Followup Data"##to make navigation up top have real words

# from simple_history import register
# register(More_Data_Page)


    # checkins = models.IntegerField(verbose_name = "Facebook Checkins", default='0000000',null=True)
    # likes = models.IntegerField(verbose_name = "Facebook Likes", default='0000000',null=True)
    # final_employees = models.IntegerField(verbose_name = "Employees (est.)", default='0000000',null=True)
    # num_loans = models.IntegerField(verbose_name = "SBA Loans (2007+)", default='0000000',null=True)
    # Revenue_Yr = models.IntegerField(verbose_name = "Revenue (est.)", default='0000000',null=True)
    # review_count = models.IntegerField(verbose_name = "Yelp Review Count", default='0000000',null=True)
    # sum_loans = models.IntegerField(verbose_name = "SBA Loan vol. (2007+)", default='0000000',null=True)
    # X2013_Employees = models.IntegerField(verbose_name = "Employees (2013 est.)", default='0000000',null=True)
    # X2013_Revenue_Yr = models.IntegerField(verbose_name = "Revenue (2013 est.)", default='0000000',null=True)
    # final_yr_incorporated = models.IntegerField(verbose_name = "Year of Incorporation", default='0000000',null=True)
    # centile = models.IntegerField(verbose_name = "Loan Likelihood Score", default='0000000',null=True)



# class Initial_Borr_List_Page(models.Model):
#     BorrName = models.CharField(max_length=150, verbose_name = "Company Name", default='0000000')
#     BorrStreet = models.CharField(max_length=150, verbose_name = "Address", default='0000000',blank=True)
#     BorrState = models.CharField(max_length=150, verbose_name = "City", default='0000000',blank=True)
#     BorrCity = models.CharField(max_length=150, verbose_name = "State", default='0000000',blank=True)
#     BorrZip = models.CharField(max_length=150, verbose_name = "ZIP Code", default='0000000',blank=True)
#     BorrCounty= models.CharField(max_length=150, verbose_name = "County", default='0000000',blank=True)
#     BorrPhoneNumber= models.CharField(max_length=150, verbose_name = "Phone Number Combined", default='0000000',blank=True)
#     BorrWebsite= models.CharField(max_length=150, verbose_name = "Website", default='0000000',blank=True)
#     BorrEmployees= models.CharField(max_length=150, verbose_name = "Number Employee (est.)", default='0000000',blank=True)
#     BorrSales= models.CharField(max_length=150, verbose_name = "Sales Volume (est.)", default='0000000',blank=True)
#     BorrAge= models.CharField(max_length=150, verbose_name = "Years In Database", default='0000000',blank=True)
#     BorrSICName= models.CharField(max_length=150, verbose_name = "Line of Business", default='0000000',blank=True)

#     Created = models.ForeignKey(DateTime, null=True)
#     FindMoreData = models.BooleanField(default=False, verbose_name = "Find More Information")
#     def __str__(self):
#         return self.BorrName
#     def get_absolute_url(self):
#         return reverse('Initial_Borr_List_Page_detail', args=[str(self.id)])
#     class Meta:
#         verbose_name_plural = "Initial Data"##to make navigation up top have real words



# class More_Data_Page(models.Model):
#     FollowUp=  models.BooleanField(default=False, verbose_name = "Contact Business")
#     # BorrName= models.ForeignKey(Initial_Borr_List_Page, null=True)
#     BorrName = models.CharField(max_length=150, verbose_name = "Company Name", default='0000000')
#     BorrOwnerName= models.CharField(max_length=150, verbose_name = "Owner Name", default='0000000',null=True)
#     BorrYelpLink= models.CharField(max_length=150, verbose_name = "Yelp link", default='0000000',null=True)
#     BorrYelpNumReviews= models.CharField(max_length=150, verbose_name = "Yelp # reviews", default='0000000',null=True)
#     BorrFacebookPage= models.CharField(max_length=150, verbose_name = "Facebook page", default='0000000',null=True)
#     BorrPreviousLender= models.CharField(max_length=150, verbose_name = "Previous lender", default='0000000',null=True)
#     BorrLastLoanDate= models.CharField(max_length=150, verbose_name = "Last loan date", default='0000000',null=True)
#     BorrLastLoanMaturity= models.CharField(max_length=150, verbose_name = "Loan maturity date", default='0000000',null=True)
#     BorrLoanType= models.CharField(max_length=150, verbose_name = "Loan type", default='0000000',null=True)
#     BorrPhoneNumberVal= models.CharField(max_length=150, verbose_name = "Validated phone", default='0000000',null=True)
#     BorrLoanProb= models.CharField(max_length=150, verbose_name = "Loan Probability", default='0000000',null=True)
#     BorrEmail= models.CharField(max_length=150, verbose_name = "Validated email", default='0000000',null=True)
#     BorrWebsiteVal= models.CharField(max_length=150, verbose_name = "Validated website", default='0000000',null=True)
#     BorrSquareft= models.CharField(max_length=150, verbose_name = "Square footage", default='0000000',null=True)
#     BorrOwnRent= models.CharField(max_length=150, verbose_name = "Own or rent", default='0000000',null=True)
#     Created = models.ForeignKey(DateTime, null=True)
#     def __str__(self):
#         return self.BorrName
#     def get_absolute_url(self):
#         return reverse('More_Data_Page_detail', args=[str(self.id)])
#     class Meta:
#         verbose_name_plural = "Followup Data"##to make navigation up top have real words