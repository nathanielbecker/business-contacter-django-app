"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^g!wjn8m0t!c*7%hj3jj@(%a@o&*oa39j9$lj7(va3&dapvnj_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    '/Users/natebecker/.virtualenvs/venv_address_booker/startover/myproject/cookie_app/templates',
    os.path.join(BASE_DIR, '/cookie_app/templates'),
    '/home/ubuntu/siter/business-contacter-django-app/myproject/cookie_app/templates',
)

# Application definition

INSTALLED_APPS = (
    # 'grappelli',###django admin interface alternative https://github.com/sehmaschine/django-grappelli
    # 'xadmin',###from https://xadmin.readthedocs.org/en/latest/quickstart.html#id2
    # 'crispy_forms',
    # 'reversion',
    'suit',###django admin interface alternative http://django-suit.readthedocs.org/en/develop/
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'floppyforms',
    'cookie_app',
    'bootstrap3',
    'django_tables2',
    # 'csvimport.app.CSVImportConf', ####note that commenting this out removes csv importer from the left-hand menu side
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')###added as per http://stackoverflow.com/questions/23215581/unable-to-perform-collectstatic

# #####note that if you uncomment this, the locally deployed website looks like what the EC2 instance has (no assets are visible)
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
#     '/home/ubuntu/siter/business-contacter-django-app/myproject/static',
#     '/Users/natebecker/.virtualenvs/venv_address_booker/startover/myproject',
# )

##########I added this for django_tables2 compatibility (see http://django-tables2.readthedocs.org/en/latest/)###also used in grappelli/django suit https://github.com/sehmaschine/django-grappelli
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.request',)
##########

######django suit configurations

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Quantile',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    'SEARCH_URL': '',# Set to empty string if you want to hide search from menu

    'MENU_ICONS': {
       'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    'MENU_EXCLUDE': ('auth.group','cookie_app.datetime'),
    'MENU': (
        'sites',
        # {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        # {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        # {'label': 'Initial Data', 'icon':' icon-tasks', 'models': ('cookie_app.Initial_Borr_List_Page'), 'url': '/admin/cookie_app/initial_borr_list_page/'},####commented out to remove initial data tag
        {'label': 'Followup Data', 'icon':'icon-ok', 'models': ('cookie_app.more_data_page'),'url': '/admin/cookie_app/more_data_page/'},
        # {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    ),

    # misc
    'LIST_PER_PAGE': 100
}



