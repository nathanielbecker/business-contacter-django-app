###set up heroku stuff

#sudo pip install python-dev
#sudo pip install  python-psycopg2

sudo pip install gunicorn
sudo pip install  dj-database-url
sudo pip install  dj-static
sudo pip install  static

libpq-dev
###from http://www.indjango.com/deploying-django-app-on-heroku/
heroku create django-business-db

git clone git@heroku.com:django-business-db.git
git clone https://git.heroku.com/django-business-db.git

heroku git:remote -a django-business-db


#####https://realpython.com/blog/python/migrating-your-django-project-to-heroku/

curl -u 'nathanielbecker' https://api.github.com/user/repos -d '{"name":"django-biz-db-deploy-heroku-s3"}'

touch README.md
git init
git add .
git commit -am "initial"
git remote add origin https://github.com/nathanielbecker/django-biz-db-deploy-heroku-s3.git
git push origin master

virtualenv django-biz-db

mkvirtualenv django-biz-db

pip install django-toolbelt
###see here if you get errors: http://www.marinamele.com/2013/12/how-to-set-django-app-on-heroku-part-i.html


pip install MySQL-python

# ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" ##install brew
# brew install mysql

mysql.server start
mysql -u root # -p
CREATE DATABASE django_deploy;
quit

pip install py-mysql2pgsql

###do shit from here to reset postgres pw ##from http://stackoverflow.com/questions/13921380/how-do-i-reset-the-postgresql-9-2-default-user-usually-postgres-password-on and http://cli23.blogspot.com/2013/12/resetting-postgresql-postgres-user.html
sudo vim /Library/PostgreSQL/9.4/data/pg_hba.conf
sudo su postgres

/Library/PostgreSQL/9.4/bin/pg_ctl restart -D /Library/PostgreSQL/9.4/data/

# postgres username = postgres, pw = pw
CREATE USER natebecker WITH ENCRYPTED PASSWORD 'pw';
# postgres username = natebecker, pw = pw
sudo ln -s /Library/PostgreSQL/9.4/lib/libssl.1.0.0.dylib /usr/lib
sudo ln -s /Library/PostgreSQL/9.4/lib/libcrypto.1.0.0.dylib /usr/lib


sudo ln -s /Applications/Postgres.app/Contents/MacOS/lib/libssl.1.0.0.dylib /usr/lib sudo ln -s /Applications/Postgres.app/Contents/MacOS/lib/libcrypto.1.0.0.dylib /usr/lib



psycopg2 module:  Symbol not found: _lo_lseek64

