# -*- coding: utf-8 -*-
"""
Django settings for students project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.conf import global_settings
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY! WARNING: don't run with debug turned on in production
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'registration', #http://django-registration-redux.readthedocs.io/en/latest/index.html
    'social_django', # Аунтификация через Facebook http://python-social-auth.readthedocs.io/en/latest/configuration/django.html
    'student',
    'students',
]

MIDDLEWARE = [
    'students.middleware.RequestTimeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

]

ROOT_URLCONF = 'students.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'student/templates',),
                 os.path.join(BASE_DIR, 'students/templates',),
                 ]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'social_django.context_processors.backends', # Аунтификация через Facebook
                'social_django.context_processors.login_redirect', # Аунтификация через Facebook
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'students.contex_processors.students_proc',
                'student.context_processors.groups_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'students.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'students',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Поддерживаемые языки
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

# переменная указывает путь к каталогу locale
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'student/locale'),
    os.path.join(BASE_DIR, 'students/locale'),
)
#print(LOCALE_PATHS)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


# Путь до папки со статическими файлами
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'student/static'),
)


# Посик статических файлов во всех папках и разделах
# https://docs.djangoproject.com/en/1.8.6/ref/settings/
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # other finders..
    #'compressor.finders.CompressorFinder', # Относится к Django Compressor

)

PORTAL_URL = 'http://127.0.0.1:8000'

# Настройки почтового сервера
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'my-email'
EMAIL_HOST_PASSWORD = 'my-password'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'my-email'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Замена заголовка входа в админку на свой и замена тайтла
from django.contrib import admin
admin.site.site_header = 'Привет админ!'
admin.site.site_title = 'Студенты'


LOG_FILE = os.path.join(BASE_DIR, 'student.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'students.signals': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'students.views.contact_admin': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        }
    }
}

# модуль django-registration-redux
REGISTRATION_OPEN = True
LOGIN_URL = 'users:auth_login'
LOGOUT_URL = 'users:auth_logout'

# Аунтификация через Facebook http://python-social-auth.readthedocs.io/en/latest/configuration/django.html
AUTHENTICATION_BACKENDS = (
'social_core.backends.facebook.FacebookOAuth2',
'django.contrib.auth.backends.ModelBackend',
 )

SOCIAL_AUTH_FACEBOOK_KEY = 'mykey'
SOCIAL_AUTH_FACEBOOK_SECRET = 'mysecret'

