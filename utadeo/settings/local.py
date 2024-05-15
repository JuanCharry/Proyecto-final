from .general import *



DEBUG = True

ALLOWED_HOSTS = []




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': 'programa',
        'USER': 'cris',
        'PASSWORD': 'cristian2003',
        'HOST': 'localhost',
        'PORT': '5432', 
    }
}


STATIC_URL = 'static/'