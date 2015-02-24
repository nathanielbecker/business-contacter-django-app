###http://www.nickpolet.com/blog/deploying-django-on-aws/1/
#####how to run EC2 instance of your site:
chmod 400 ~/Desktop/key_pair_CA_2.pem
ssh -i ~/Desktop/key_pair_CA_2.pem ubuntu@54.153.63.147
########
sudo apt-get update
sudo apt-get install apache2 libapache2-mod-wsgi
sudo apt-get install python-pip
sudo pip install django
sudo apt-get install python-psycopg2
sudo apt-get install git

cd ~
mkdir siter
cd siter
django-admin.py startproject business_prospector
git clone https://github.com/nathanielbecker/business-contacter-django-app.git
sudo vim /etc/apache2/sites-enabled/siter.conf
###modify the apache config file as per the instructions###in vim you could search/replace using ':%s/business_prospector/myproject/g'
sudo pip install django-suit
sudo pip install django-floppyforms
sudo pip install django-bootstrap3
sudo pip install django-tables2

python manage.py collectstatic
sudo service apache2 restart

####move db file to ec2 server
sudo scp -i ~/Desktop/key_pair_CA_2.pem db.sqlite3 ubuntu@ec2-54-153-72-36.us-west-1.compute.amazonaws.com:~/.


sudo chown www-data myproject/
sudo chown www-data myproject/db.sqlite3

/home/ubuntu/siter/business-contacter-django-app/myproject/static
/home/ubuntu/siter/business-contacter-django-app/myproject/media

#####you NEED to add an alias for /static/, see http://stackoverflow.com/questions/25368885/amazon-ec2-django-static-files-configuration, basically add this line to wsgi something "Alias /static/ /home/ubuntu/siter/business-contacter-django-app/myproject/static/"


