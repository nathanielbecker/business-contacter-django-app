import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^g!wjn8m0t!c*7%hj3jj@(%a@o&*oa39j9$lj7(va3&dapvnj_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    # '/Users/natebecker/.virtualenvs/venv_address_booker/startover/myproject/cookie_app/templates',
    os.path.join(BASE_DIR, '/cookie_app/templates'),
)
print(TEMPLATE_DIRS)
