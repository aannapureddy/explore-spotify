"""
Django settings for feed_spotify project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'spotify_hits',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
    },
}


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+0o46&ih-6(y==9joo700sf@6h#0g9q&zhm=vz+qehq&0+wu0h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'spotify',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'feed_spotify.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'feed_spotify.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

COUNTRIES = {
'global': 'Global',
'us': 'United States',
'gb': 'United Kingdom',
'ad': 'Andorra',
'ar': 'Argentina',
'at': 'Austria',
'au': 'Australia',
'be': 'Belgium',
'bg': 'Bulgaria',
'bo': 'Bolivia',
'br': 'Brazil',
'ca': 'Canada',
'ch': 'Switzerland',
'cl': 'Chile',
'co': 'Colombia',
'cr': 'Costa Rica',
'cy': 'Cyprus',
'cz': 'Czech Republic',
'de': 'Germany',
'dk': 'Denmark',
'do': 'Dominican Republic',
'ec': 'Ecuador',
'ee': 'Estonia',
'es': 'Spain',
'fi': 'Finland',
'fr': 'France',
'gr': 'Greece',
'gt': 'Guatemala',
'hk': 'Hong Kong',
'hn': 'Honduras',
'hu': 'Hungary',
'id': 'Indonesia',
'ie': 'Ireland',
'il': 'Israel',
'in': 'India',
'is': 'Iceland',
'it': 'Italy',
'jp': 'Japan',
'lt': 'Lithuania',
'lu': 'Luxembourg',
'lv': 'Latvia',
'mc': 'Monaco',
'mt': 'Malta',
'mx': 'Mexico',
'my': 'Malaysia',
'ni': 'Nicaragua',
'nl': 'Netherlands',
'no': 'Norway',
'nz': 'New Zealand',
'pa': 'Panama',
'pe': 'Peru',
'ph': 'Philippines',
'pl': 'Poland',
'pt': 'Portugal',
'py': 'Paraguay',
'ro': 'Romania',
'se': 'Sweden',
'sg': 'Singapore',
'sk': 'Slovakia',
'sv': 'El Salvador',
'th': 'Thailand',
'tr': 'Turkey',
'tw': 'Taiwan',
'uy': 'Uruguay',
'vn': 'Viet Nam',
'za': 'South Africa'
}