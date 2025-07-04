"""
Django settings for panic_button project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta
from decouple import config
import cloudinary
import cloudinary.uploader
import cloudinary.api
import pymysql
pymysql.install_as_MySQLdb()
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DATA_UPLOAD_MAX_MEMORY_SIZE = 1073741824  
FILE_UPLOAD_MAX_MEMORY_SIZE = 1073741824  

DEBUG = True
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    'https://emergency-trigger-sos-production.up.railway.app',
    # 'http://182.72.203.255:8058', 
    'http://192.168.137.1:8000',
]
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]

CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
]
CSRF_TRUSTED_ORIGINS = [
    # 'https://www.Emergency Trigger.com',  
    # 'https://Emergency Trigger.com',  
    # 'https://stg.Emergency Trigger.com',  
    # 'https://www.stg.Emergency Trigger.com',  
    # 'http://182.72.203.255:8058',
    'https://emergency-trigger-sos-production.up.railway.app/',
    'http://192.168.137.1:8000/', 
]

# SITE_URL = 'https://Emergency Trigger.com' 
# SITE_URL='http://192.168.137.1:8000'
SITE_URL='https://emergency-trigger-sos-production.up.railway.app'
# SITE_URL = 'https://stg.Emergency Trigger.com' 
# SITE_URL = 'http://192.168.1.2:8000'
# SITE_URL = 'http://172.16.1.247:8000'

# SITE_URL = config('SITE_URL')
STREAM_BASE_URL = config('STREAM_BASE_URL')


LOGIN_URL = '/'
LOGOUT_URL = '/'

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# WhatsApp
WHATSAPP_ACCESS_TOKEN = config('WHATSAPP_ACCESS_TOKEN')
WHATSAPP_PHONE_NUMBER_ID = config('WHATSAPP_PHONE_NUMBER_ID')
WHATSAPP_API_URL = f"https://graph.facebook.com/v17.0/{WHATSAPP_PHONE_NUMBER_ID}/messages"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get("REDIS_URL", "redis://127.0.0.1:6379/1"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Twilio
# TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
# TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
# TWILIO_PHONE_NUMBER = config('TWILIO_PHONE_NUMBER')
# TWILIO_WHATSAPP_LINK = 'http://wa.me/+14155238886?text=join%20popular-clearly'
TWILIO_WHATSAPP_LINK = 'http://wa.me/+14155238886?text=join%20face-quiet'
TWILIO_ACCOUNT_SID=config('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN=config('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER=config('TWILIO_PHONE_NUMBER')
RAZORPAY_API_KEY = config('RAZORPAY_API_KEY')
RAZORPAY_API_SECRET = config('RAZORPAY_API_SECRET')



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'no.reply.icebutton@gmail.com'  
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True 
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')





# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'cloudinary',
    'cloudinary_storage',
    'drf_yasg',
    'django_apscheduler',
    'ckeditor',
    'core',
    'customadmin',
    'blogs',
    'widget_tweaks',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'core.middleware.Custom404Middleware',
    'core.middleware.BasicAuthMiddleware',  # ✅ Replace 'yourapp' with your app name
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'panic_button.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', BASE_DIR / 'customadmin/templates'],
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

WSGI_APPLICATION = 'panic_button.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases



# #################### Staging Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'newdb_sos',
#         'USER': 'kanik-snippet',
#         'PASSWORD': 'Snippet@1',
#         # 'HOST': 'db',
#         'HOST':'127.0.0.1',
#         'PORT': '3306',
#     }
# }


# #################### Prod Database

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
    )
}

LANGUAGE_CODE = 'en'  # Default language
USE_I18N = True  # Enable internationalization
USE_L10N = True  # Enable localized formatting
USE_TZ = True    # Enable timezone support

LANGUAGES = [
    ('en', 'English'),
    ('hi', 'Hindi'),
]
LOCALE_PATHS = [BASE_DIR / 'locale']
LANGUAGE_COOKIE_NAME = 'django_language'

# Password validation

# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'core.auth_backends.BaseUserBackend', 
    'django.contrib.auth.backends.ModelBackend',
]



# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/


TIME_ZONE = 'Asia/Kolkata'  

USE_TZ = True  

USE_I18N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'customadmin.BaseUser'

# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',  # Default to JSON renderer
#     ],
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),  
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'BLACKLIST_ENABLED': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
    'DEFAULT_API_URL': SITE_URL,
}


CRON_CLASSES = [
    'core.cron.ExpirePlansCronJob',
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'diutbnbh6',
    'API_KEY': '199663559681182',
    'API_SECRET': '_XgNMYshbeP6S02vdDF3IWiteaQ',
    'RESOURCE_TYPE': 'video',
    'UPLOAD_OPTIONS': {
        'resource_type': 'video',
    }
}

IP_GEOLOCATION_API_KEY = 'a71c0d83d391ec'

cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET']
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'



