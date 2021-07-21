"""
Django settings for a project.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import json
import sys

from django.core.exceptions         import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR                = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(f"BASE_DIR = {BASE_DIR}")
EXTERNAL_BASE           = os.path.join(BASE_DIR, "externals")
EXTERNAL_LIBS_PATH      = os.path.join(EXTERNAL_BASE, "libs")
EXTERNAL_APPS_PATH      = os.path.join(EXTERNAL_BASE, "apps")
sys.path                = ["", EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path


with open(os.path.join(os.path.dirname(__file__), 'secrets.json'), 'r') as f:
    secrets             = json.loads(f.read())

def get_secret(setting):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg       = f'Set the {setting} secret variable'
        raise ImproperlyConfigured(error_msg)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY              = get_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG                   = True

ALLOWED_HOSTS           = [
      "127.0.0.1"
    , "0.0.0.0"
    , "localhost"
]


# Application definition
INSTALLED_APPS          = [
    # contributed
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third-party
    # ...
    # local
    'src.apps.core'
]

MIDDLEWARE              = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF            = 'src.urls'

TEMPLATES               = [
    {
        'BACKEND'       : 'django.template.backends.django.DjangoTemplates',
        'DIRS'          : [os.path.join(BASE_DIR, 'src', 'templates')],
        'APP_DIRS'      : True,
        'OPTIONS'       : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION        = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
          'ENGINE'       : 'django.db.backends.postgresql_psycopg2'
        , 'NAME'         : get_secret('DATABASE_NAME')
        , 'USER'         : get_secret('DATABASE_USER')
        , 'PASSWORD'     : get_secret('DATABASE_PASSWORD')
        , 'HOST'         : get_secret('DATABASE_HOST')
        , 'PORT'         : get_secret('DATABASE_PORT')
    }}


# Password validation
# https://docs.djangoproject.com/en/3.1/topics/auth/passwords/#password-validation

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LOCALE_PATHS            = [
    os.path.join(BASE_DIR, 'locale'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_DIRS        = [
      os.path.join(BASE_DIR, 'src', 'site_static')
]

print(STATICFILES_DIRS)

STATIC_ROOT             = os.path.join(BASE_DIR, 'static')
STATIC_URL              = f'static/'
print(STATIC_ROOT)

MEDIA_URL               = '/media/'
MEDIA_ROOT              = os.path.join(BASE_DIR, 'media')