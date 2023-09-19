from .base import *
from decouple import config


SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)


ALLOWED_HOSTS = ["*"]




DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'history.apps.HistoryConfig',
]

THIRRD_PACKEGES =[
    'rest_framework',
    'decouple',
    'django_filters',
    'corsheaders',
    'easy_thumbnails'
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRRD_PACKEGES


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('db_name'),
        'USER':'postgres',
        'PASSWORD':config('db_ps'),
        'PORT':config('port'),
        'HOST':config('host'),
    }
}


# CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://localhost:8000",
# ]

# CSRF_TRUSTED_ORIGINS = ['http://localhost:3000']
