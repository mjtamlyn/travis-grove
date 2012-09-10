# Django settings for practicals project.
import os

import dj_database_url


DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

DEBUG = bool(os.environ.get('DEBUG', False))

DATABASES = {'default': dj_database_url.config(default='postgres://localhost/travis_grove')}

ADMINS = (('Admin', 'marc.tamlyn@gmail.com'),)
MANAGERS = ADMINS
ADMIN_EMAILS = zip(*ADMINS)[1]
EMAIL_SUBJECT_PREFIX = '[practicals] '
SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'marc.tamlyn@gmail.com'
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

TIME_ZONE = 'UTC'
USE_L10N = True  # Locale
USE_TZ = True

LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-GB')
USE_I18N = True  # Internationalization

# Static
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (os.path.join(DIRNAME, 'templates'),)

ROOT_URLCONF = 'travis_grove.urls'
SECRET_KEY = 'o$-hdw5%tq@ijxs9&r3*$y57v8b!wlfjadus(2k&a4s8qiu'
SITE_ID = 1
WSGI_APPLICATION = 'travis_grove.wsgi.application'

INSTALLED_APPS = (
    'travis_grove',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
