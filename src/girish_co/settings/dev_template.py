from .base import *

DEBUG = True

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = True

SECRET_KEY = ''


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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

OPBEAT = {
    'ORGANIZATION_ID': '',
    'APP_ID': '',
    'SECRET_TOKEN': '',
}