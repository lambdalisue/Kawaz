# -*- coding: utf-8 -*-
# Django settings for Kawaz project.
import sys
import os.path
ROOT = os.path.join(os.path.dirname(__file__), '../../')
#--- Add PYTHON_PATH ---------------------------------
PYTHON_PATHS = (
    os.path.join(ROOT, 'src/libs'),
)
for path in PYTHON_PATHS:
    if path not in sys.path: sys.path.append(path)
#-----------------------------------------------------

# Version of Kawaz
VERSION = '0.31415rc1'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Tokyo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ja'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(ROOT, 'statics/media'),

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'media'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(ROOT, 'static/collected')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'mfw.template.loaders.flavour.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'mfw.middleware.session.SessionMiddleware',
    'mfw.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'mfw.middleware.device.DeviceDetectionMiddleware',
    'mfw.middleware.emoji.DeviceEmojiTranslationMiddleware',
    'mfw.middleware.flavour.DeviceFlavourDetectionMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "mfw.core.context_processors.device",
    "mfw.core.context_processors.flavour",
)

ROOT_URLCONF = 'Kawaz.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT, 'templates'),
    os.path.join(ROOT, 'templates/default'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    # Third-party libraries
    'south',                        # Database migration library
    'compress',                     # JavaScript/CSS compress library
    'reversetag',                   # Useful templatetag library
    'pagination',                   # Useful paginatin library
    'haystack',                     # Search engine library
    'registration',                 # Registration library
    'piston',                       # Django API library
    'markupfield',                  # Markup field library
    # Github libraries
    'qwert',                        # Useful snippet collection library
    'mfw',                          # Django mobile framework library
    'object_permission',            # Object permission library
    'universaltag',                 # Django universal tagging library
    'googlemap',                    # Django googlemap library
    # Kawaz apps
    'Kawaz.globals',
    'Kawaz.announcements',
)

LOGIN_REDIRECT_URL  = "/"
LOGIN_URL = "/registration/login/"
LOGOUT_URL = "/registration/logout/"

# --- django-googlemap
GOOGLEMAP_API_SENSOR = True

# --- django-haystack
HAYSTACK_SITECONF = 'Kawaz.search_sites'
HAYSTACK_DEFAULT_OPERATOR = 'OR'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(ROOT, 'whoosh')


try:
    from local_settings import *
except ImportError:
    raise ImportError("Copy `local_settings.sample.py` to `local_settings.py` and configure it.")