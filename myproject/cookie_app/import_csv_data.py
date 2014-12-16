############from http://stackoverflow.com/questions/1882469/how-do-i-transfer-data-in-csv-file-into-my-sqlite-database-in-django############
###this only works when you physically run it in python, not from command line *shrug*
# Full path and name to your csv file
csv_filepathname="/Users/natebecker/.virtualenvs/venv_address_booker/startover/myproject/4good_candidate_business_names.csv"
# Full path to the directory immediately above your django project directory
your_djangoproject_home="/Users/natebecker/.virtualenvs/venv_address_booker/startover/"
############ All you need to modify is above ############
# from django.core.management.base import BaseCommand, CommandError

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] ='myproject.settings'

from cookie_app.models import Initial_Borr_List_Page, DateTime

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter='\t', quotechar='"')

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

