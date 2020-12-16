from .base import *

DEBUG = False

DATABASES = DATABASES['mysql']

ALLOWED_HOSTS = '*'

# Cross domain request 를 허용할 호스트
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = []
