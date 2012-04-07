# Django settings for barcampboston project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'America/New_York'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

STATIC_URL = '/static/'

# the below is a default that should work for most sites,
# but was needed in particular for Django Zoom
import os
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(ROOT_PATH, "static")

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'barcampboston.urls'

INSTALLED_APPS = (
    'barcampboston.attendees',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'treemenus',
    'sorl.thumbnail',
    'taggit',
    'django_gravatar',
)

try:
    from local_django_settings import *
except:
    pass
