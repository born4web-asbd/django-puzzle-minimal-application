"""
Django settings for minimalpuzzle project.
"""
import os
from pathlib import Path
from django.contrib.messages import constants as messages
from django.utils.translation import gettext_lazy as _
from .production_allowed_hosts import PRODUCTION_ALLOWED_HOSTS
from sharedlibrary.configurations.summernote_wysiwyg import ASBD_SUMMERNOTE_THEME, ASBD_SUMMERNOTE_CONFIG

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Application identifier/name used to get and switch application specific configurations for modules
DJANGO_PUZZLE_APPLICATION = 'minimalpuzzle'
DJANGO_PUZZLE_APPLICATION_CONFIG = {
    'SETTINGS_DIR': BASE_DIR / DJANGO_PUZZLE_APPLICATION,
    'CONFIGURATIONS': f"{DJANGO_PUZZLE_APPLICATION}.configurations",
    # 'TEMPLATES': BASE_DIR / DJANGO_PUZZLE_APPLICATION / 'templates',
    'TEMPLATES': BASE_DIR / 'sharedlibrary' / 'templates',
    # Implemented django puzzles or app modules - we can use it for management commands over our modules for example
    'IMPLEMENTED_MODULES': [
        # 'sharedlibrary', TODO: Zkontrolovat jestli to neni nekde pouzito ale logicky to sem nepatri !!!
        'accounts',
        'contacts',
        'textnote',
        'feedback',
        # 'byty',
        # 'sluzby',
        # 'uzaverky',
        # 'odecty',
    ]
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3$ynm(2td_v5+d+)h+1x6p9jz$_&nmu7dd_$wd5_bqwnzv5oju'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = PRODUCTION_ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aplikace tretich stran
    'django_extensions',
    'phonenumber_field',
    'mathfilters',
    'django_summernote',  # WYSIWYG
    # 'bootstrap4',
    'bootstrap5',
    # 'bootstrap_datepicker_plus',
    # 'fontawesomefree',

    # REST API framework
    # 'rest_framework',

    # PUZZLES
    'sharedlibrary',
    'accounts',
    'contacts',
    'textnote',
    'feedback',

    # ASBD
    # 'byty',
    # 'sluzby',
    # 'uzaverky',
    # 'odecty',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'minimalpuzzle.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            DJANGO_PUZZLE_APPLICATION_CONFIG["TEMPLATES"],
            BASE_DIR / 'sharedlibrary' / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # User defined context processors
                'sharedlibrary.context_processors.django_puzzle_application_name',
                'sharedlibrary.context_processors.back_link_referer',
                'sharedlibrary.context_processors.django_puzzle_installed_applications',
                'sharedlibrary.context_processors.django_puzzle_context_parameters_configuration',
                'sharedlibrary.context_processors.django_puzzle_implemented_modules',
                'sharedlibrary.context_processors.django_puzzle_navbar',
                'accounts.utils.context_processors.is_user_deletion_allowed_from_application',
                'accounts.utils.context_processors.is_user_member_of_developers',
            ],
        },
    },
]

WSGI_APPLICATION = 'minimalpuzzle.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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


LANGUAGES = [
    ('cs', _('Czech')),
    ('en', _('English')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale'
]

# Internationalization
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'cs'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static_deployment'

STATICFILES_DIRS = [
    BASE_DIR / 'static_shared',
    DJANGO_PUZZLE_APPLICATION_CONFIG["TEMPLATES"] / 'static',
    BASE_DIR / 'sharedlibrary' / 'templates' / 'static',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# FILE SYSTEM STORAGE SETTINGS
MEDIA_URL = '/filestorage/'
MEDIA_ROOT = BASE_DIR / 'filestorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'hide_log_level_names': {
            '()': 'sharedlibrary.utils.logging.FilterLogLevelNames',
            'log_level_names': [],
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'csv_log_file_format': {
            'format': '%(asctime)s; %(name)s; %(levelname)s; %(message)s; %(pathname)s; %(lineno)s; %(args)s;',
            # 'format': '%(asctime)s; %(name)-12s %(levelname;)-8s %(message;)s %(pathname)s; %(lineno)s; %(args)s;',
            # 'datefmt' : "%d/%b/%Y %H:%M:%S"
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / os.getenv('APPLICATION_LOG_FILE'),
            'maxBytes': 5242880,
            'backupCount': 100,
            'formatter': 'csv_log_file_format'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins', 'log_file'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

# MESSAGES PODPORA - BOOTSTRAP
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# WYSIWYG editor podpora
SUMMERNOTE_THEME = ASBD_SUMMERNOTE_THEME
SUMMERNOTE_CONFIG = ASBD_SUMMERNOTE_CONFIG

# TEST SERVER INTERNET ACCESS
# CORS_REPLACE_HTTPS_REFERER = False
# HOST_SCHEME = "http://"
# SECURE_PROXY_SSL_HEADER = None
# SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False
# SECURE_HSTS_SECONDS = None
# SECURE_HSTS_INCLUDE_SUBDOMAINS = False
# SECURE_FRAME_DENY = False
