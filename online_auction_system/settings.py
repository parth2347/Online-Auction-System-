"""
Django settings for online_auction_system project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import json
import os
import dj_database_url

from django.core.exceptions import ImproperlyConfigured

with open('secrets-template.json') as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)

LOGIN_REDIRECT_URL = "view_product"
LOGIN_URL = "/accounts/login/"

LOGOUT_REDIRECT_URL = "/accounts/login/"
LOGOUT_URL = "/accounts/logout/"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

SECRET_KEY = get_secret('SECRET_KEY')
DEBUG = bool(get_secret('DEBUG'))
ALLOWED_HOSTS = [get_secret('ALLOWED_HOSTS')]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auction_system',
]
INSTALLED_APPS += ('storages',)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'online_auction_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'online_auction_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
   'default': {
   'ENGINE': 'django.db.backends.sqlite3',
   'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/auction_system/static/'
STATIC_ROOT = BASE_DIR

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + MEDIA_URL

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'auction_system/static'),
    os.path.join(BASE_DIR, 'media'),
)


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = get_secret('GMAIL_SMTP_USER')
EMAIL_HOST_PASSWORD = get_secret('GMAIL_SMTP_PASSWORD')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# AWS_QUERYSTRING_AUTH = False
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
# MEDIA_URL = 'http://%s.s3.amazonaws.com/picktheproducts/' % AWS_STORAGE_BUCKET_NAME
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

PAYPAL_RECEIVER_EMAIL = get_secret('PAYPAL_EMAIL')
PAYPAL_TEST = True
