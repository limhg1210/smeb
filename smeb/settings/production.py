from .base import *

DEBUG = False

DATABASES = DATABASES['mysql']

ALLOWED_HOSTS = '*'

# Cross domain request 를 허용할 호스트
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = []

# Mail

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = EMAIL_HOST
EMAIL_PORT = EMAIL_PORT
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = True
