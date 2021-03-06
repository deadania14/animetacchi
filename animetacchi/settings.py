# Django settings for animetacchi project.

import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
        'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(PROJECT_PATH, 'db.sqlite3'),
                }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

# CAPTCHA SETTINGS
CAPTCHA_FONT_PATH = os.path.join(PROJECT_PATH, 'courier.ttf')
CAPTCHA_FONT_SIZE = 34

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#rj!&#1rml6u81l!lm8w1$u_1=+(e1gd88i!51irap(b_omv8k'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
     #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    #'animetacchi.middleware.DefaultMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'responsive.middleware.DeviceInfoMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#SOCIAL_AUTH_USER_MODEL = 'numflo.CustomUser'

LOGIN_URL = '/signin/'
ROOT_URLCONF = 'animetacchi.urls'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
#SOCIAL_AUTH_USER_MODEL = 'numflo.Student'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'responsive.context_processors.device_info'
)

DEFAULT_BREAKPOINTS = {
    'phone': 480,
    'tablet': 767,
    'desktop': None,
}

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'animetacchi.wsgi.application'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'belajarpython101@gmail.com'
EMAIL_HOST_PASSWORD = 'wedontt4lk4boutphp'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL='(Backend) bepy <no-reply@backend.com>'


# compression setup
COMPRESS_ENABLED = True
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_URL = MEDIA_URL
COMPRESS_ROOT = MEDIA_ROOT
COMPRESS_PARSER = 'compressor.parser.LxmlParser'

DJANGO_WYSIWYG_FLAVOR = "tinymce_advanced"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
 #   'django_wysiwyg',
 #   'compressor',
    'animetacchi',
 #   'captcha',
    'south',
#    'social_auth',
    'responsive',
#    'easy_thumbnails',
#    'import_export',
    'djcelery',
    'service',
#    'mathfilters',

    #eksternal app
    'ratings',
    'vote',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
    'djcelery': 'djcelery.south_migrations',
}

