import os

from .base import * # noqa


DEBUG = True
ALLOWED_HOSTS = ['*']
DEV = DEBUG

INSTALLED_APPS += ()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    },
}

MIDDLEWARE += ()

SECRET_KEY = 'devel'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 2

AUTH_PASSWORD_VALIDATORS = []