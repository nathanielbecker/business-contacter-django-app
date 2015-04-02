

sudo pip install django

#to get sublimetext to open via command line
open /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl
ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sublime
sublime filename (opens things in sublime)

##this code allows you to deploy a django app on AWS

#grab IP address from AWS public IP thing
ssh -i key_pair_CA_1.pem ubuntu@54.67.15.73

sudo apt-get update
sudo apt-get install apache2 libapache2-mod-wsgi
sudo apt-get install python-pip
sudo pip install django
sudo apt-get install mysql-server python-mysqldb
##root user password is: mysqlpwwee
sudo apt-get install git


django-admin.py startproject testproject

sudo vim /etc/apache2/sites-enabled/test_site.com.conf
sudo vim ~/etc/apache2/sites-enabled/address_book_test

python manage.py startapp address_booker

mkvirtualenv venv_address_booker


cookiecutter https://github.com/wildfish/cookiecutter-django-crud.git
pip install django-floppyforms

find . -name 'floppyforms'

# add shit to your settings.py in the parent project folder

    'floppyforms',
    'myproject.cookie_app',



python manage.py test myproject.cookie_app

django-admin.py startproject myproject

# so the project name is myproject
# the app name is cookie_app
# the model name is barebones_CRUD

db username is admin
pw is pw

#you gotta makemigrations then migrate for every change
python manage.py syncdb cookie_app

python manage.py makemigrations cookie_app
python manage.py migrate cookie_app
python manage.py runserver

admin username is admin2
pw is pw

pip install django-csvimport

python manage.py syncdb


.separator "\t"
.import 4good_candidate_business_names.csv cookie_app_initial_borr_list_page

# pip install django-tables2

# to kill errant dev website hosting:
ps aux | grep -i manage
kill -9 11130


find . -name 'change_list.html'
/Users/natebecker/.virtualenvs/venv_address_booker/lib/python2.7/site-packages/django/contrib/admin/templates/admin/change_list.html


git push -u origin master

###admin login
admin name: admin
pw: pw9

###admin login
name: test_lender
pw: pw9

#####login for Angela Machado
amachado
celtic

#####login for David Coffey
dcoffey
ablsba

#####login for Erik Rajek
erajek
ridgestone

#####login for Jonathan Thrasher
jthrasher
bridgeview

#####login for Mike McGrane
mmcgrane
pacific

#####login for Steve Penza
spenza
cbc

#####login for Matthew Putnam
mputnam
yadkin

#####login for Jesse Cruz
jcruz
jc8cj83

#####login for Claudia Millington
cmillington
cortrustMN

#####login for Melanie Brown
mbrown
signatureGA1

#####login for Wade stringfield
wstringfield
ccommunity

#####login for Bill Hand
bhand
pacwestcdc

#####login for Dale Hayden
dhayden
homebankoc

#####login for Chris Schmidt
cschmidt
banner8

#####login for Mike Fitzpatrick
mfitzpatrick
commercewest4

#####login for Eriasi Akridge
eakridge
bridgeb4


###insert statement moving initial_page stuff to next_page
insert into cookie_app_more_data_page SELECT * FROM cookie_app_initial_borr_list_page where  centile > 95 and Physical_State = 'CA' ORDER BY RANDOM() LIMIT 100;

drop table deleter;
create table deleter as select * from cookie_app_initial_borr_list_page order by random();
delete from cookie_app_initial_borr_list_page;
insert into cookie_app_initial_borr_list_page select * from deleter;

create table ang_backup as select * from cookie_app_more_data_page;


####install django suit
pip install django-suit


#####to deploy on EC2, you NEED to add an alias for /static/, see http://stackoverflow.com/questions/25368885/amazon-ec2-django-static-files-configuration, basically add this line to wsgi something "Alias /static/ /home/ubuntu/siter/business-contacter-django-app/myproject/static/"


#####add in django admin history module to log all changes that are made to data in models
pip install django-simple-history
##try 2
pip install django-versioning


