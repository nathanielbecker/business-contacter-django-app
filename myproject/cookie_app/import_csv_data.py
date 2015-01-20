############from http://stackoverflow.com/questions/1882469/how-do-i-transfer-data-in-csv-file-into-my-sqlite-database-in-django############
###this only works when you physically run it in python, not from command line *shrug*
# Full path and name to your csv file
csv_filepathname="/Users/natebecker/.virtualenvs/venv_address_booker/startover/myproject/fake_moredata.csv"
# Full path to the directory immediately above your django project directory
your_djangoproject_home="/Users/natebecker/.virtualenvs/venv_address_booker/startover/"
############ All you need to modify is above ############
# from django.core.management.base import BaseCommand, CommandError

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] ='myproject.settings'

from cookie_app.models import Initial_Borr_List_Page, DateTime, More_Data_Page

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    initial_borr_list_page=Initial_Borr_List_Page()
    initial_borr_list_page.BorrCity=row[1]
    initial_borr_list_page.BorrName=row[2]
    initial_borr_list_page.BorrState=row[3]
    initial_borr_list_page.BorrStreet=row[4]
    initial_borr_list_page.FindMoreData=row[5]
    # initial_borr_list_page.Created=row[6]
    initial_borr_list_page.BorrAge=row[7]
    initial_borr_list_page.BorrCounty=row[8]
    initial_borr_list_page.BorrEmployees=row[9]
    initial_borr_list_page.BorrPhoneNumber=row[10]
    initial_borr_list_page.BorrSICName=row[11]
    initial_borr_list_page.BorrSales=row[12]
    initial_borr_list_page.BorrWebsite=row[13]
    initial_borr_list_page.BorrZip=row[14]
    initial_borr_list_page.save()


for row in dataReader:
    more_data_page=More_Data_Page()
    more_data_page.BorrName=row[0]
    more_data_page.FollowUp=row[1]
    more_data_page.BorrYelpLink=row[2]
    more_data_page.BorrYelpNumReviews=row[3]
    more_data_page.BorrFacebookPage=row[4]
    more_data_page.BorrPreviousLender=row[5]
    more_data_page.BorrLastLoanDate=row[6]
    more_data_page.BorrLastLoanMaturity=row[7]
    more_data_page.BorrLoanType=row[8]
    more_data_page.BorrPhoneNumberVal=row[9]
    more_data_page.BorrLoanProb=row[10]
    more_data_page.BorrEmail=row[11]
    more_data_page.BorrWebsiteVal=row[12]
    more_data_page.BorrSquareft=row[13]
    more_data_page.BorrOwnRent=row[14]
    more_data_page.BorrOwnerName=row[15]
    more_data_page.save()


FollowUp
BorrYelpLink
BorrYelpNumReviews
BorrFacebookPage
BorrPreviousLender
BorrLastLoanDate
BorrLastLoanMaturity
BorrLoanType
BorrPhoneNumberVal
BorrLoanProb
BorrEmail
BorrWebsiteVal
BorrSquareft
BorrOwnRent
BorrOwnerName




#####previous csv/xls import tries (scrap)

# pip install data-importer

from data_importer.importers import CSVImporter
class MyCSVImporterModel(CSVImporter):
     fields = ['concatname', 'BorrName', 'BorrStreet', 'BorrState', 'BorrCity', 'BorrZip']
     class Meta:
         delimiter = "\t"
         ignore_first_line='True'

my_csv_list = MyCSVImporterModel(source='good_candidate_business_names.csv')
row, first_line = my_csv_list.cleaned_data[0]
first_line['BorrName']



from data_importer.importers import CSVImporter
from data_importer.model import MyModel
class MyCSVImporterModel(CSVImporter):
     class Meta:
         delimiter = "\t"
         model = MyModel