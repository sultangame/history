from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-n#i5@skh$b_df#2u@w7s9d#28tau20wm52-&@!31tkdw4#70iq'


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
    'easy_thumbnails',

]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRRD_PACKEGES



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://localhost:8000",
# ]

# CSRF_TRUSTED_ORIGINS = ['http://localhost:3000']