from .base import *

DEBUG = True

DATABASES = DATABASES['sqlite3']

ALLOWED_HOSTS = '*'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Mail

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
