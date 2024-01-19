import os 
from .settings import *
from .settings import BASE_DIR


SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

# WhiteNoise configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] 

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> e2bab8f2e1c705019d5369ddc52d450bc738d64f
sqlite_db_path = os.environ.get('DJANGO_SQLITE_DB_PATH', 'default.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': sqlite_db_path,
    }
<<<<<<< HEAD
}
=======
}
=======
conn_str = os.environ['AZURE_SQLITE3_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': conn_str_params['dbname'],
    }
}

# conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
# conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': conn_str_params['dbname'],
#         'HOST': conn_str_params['host'],
#         'USER': conn_str_params['user'],
#         'PASSWORD': conn_str_params['password'],
#     }
# }
>>>>>>> fa76898c7c21cb532ee1ad4e07e1a675ef07fc78
>>>>>>> e2bab8f2e1c705019d5369ddc52d450bc738d64f
