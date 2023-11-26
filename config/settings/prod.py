from .base import *

ALLOWED_HOSTS = ['was', '127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': '1q2w3e4r',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = []