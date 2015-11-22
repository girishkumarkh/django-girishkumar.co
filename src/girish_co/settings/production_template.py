from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

SECRET_KEY = ''

OPBEAT = {
    'ORGANIZATION_ID': '',
    'APP_ID': '',
    'SECRET_TOKEN': '',
}

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': '',
         'USER': '',
         'PASSWORD': '',
         'HOST': '',
         'PORT': '5432',
    }
}