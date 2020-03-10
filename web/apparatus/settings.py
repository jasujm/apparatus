"""
Django settings for apparatus project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy as _
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    DATA_DIR=(str, os.path.dirname(os.path.dirname(__file__))),
    DJANGO_LOG_LEVEL=(str, "INFO"),
)
# reading .env file
environ.Env.read_env(env.str("ENV_PATH", ".env"))

DATA_DIR = env("DATA_DIR")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

if DEBUG:
    INTERNAL_IPS = ["127.0.0.1"]


if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler",},},
    "loggers": {
        "django": {"handlers": ["console"], "level": env("DJANGO_LOG_LEVEL"),},
    },
}

# Application definition


ROOT_URLCONF = "apparatus.urls"


WSGI_APPLICATION = "apparatus.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "Europe/Amsterdam"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(DATA_DIR, "media")
STATIC_ROOT = os.path.join(DATA_DIR, "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "apparatus", "static"),)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

SITE_ID = 1

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "apparatus", "templates"),],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.template.context_processors.csrf",
                "django.template.context_processors.tz",
                "sekizai.context_processors.sekizai",
                "django.template.context_processors.static",
                "cms.context_processors.cms_settings",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]


MIDDLEWARE = [
    # Develop time middleware, should not affect behavior in prod
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "cms.middleware.utils.ApphookReloadMiddleware",
    # htmlmin -- if ever add cache, check how this should interact:
    # https://pypi.org/project/django-htmlmin/
    "htmlmin.middleware.HtmlMinifyMiddleware",
    "htmlmin.middleware.MarkRequestMiddleware",
    # Other middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
]

INSTALLED_APPS = [
    "djangocms_admin_style",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django.contrib.messages",
    "cms",
    "menus",
    "sekizai",
    "treebeard",
    "djangocms_text_ckeditor",
    "filer",
    "easy_thumbnails",
    "aldryn_apphooks_config",
    "parler",
    "taggit",
    "taggit_autosuggest",
    "meta",
    "sortedm2m",
    "djangocms_blog",
    "djangocms_bootstrap4",
    "djangocms_bootstrap4.contrib.bootstrap4_alerts",
    "djangocms_bootstrap4.contrib.bootstrap4_badge",
    "djangocms_bootstrap4.contrib.bootstrap4_card",
    "djangocms_bootstrap4.contrib.bootstrap4_carousel",
    "djangocms_bootstrap4.contrib.bootstrap4_collapse",
    "djangocms_bootstrap4.contrib.bootstrap4_content",
    "djangocms_bootstrap4.contrib.bootstrap4_grid",
    "djangocms_bootstrap4.contrib.bootstrap4_jumbotron",
    "djangocms_bootstrap4.contrib.bootstrap4_link",
    "djangocms_bootstrap4.contrib.bootstrap4_listgroup",
    "djangocms_bootstrap4.contrib.bootstrap4_media",
    "djangocms_bootstrap4.contrib.bootstrap4_picture",
    "djangocms_bootstrap4.contrib.bootstrap4_tabs",
    "djangocms_bootstrap4.contrib.bootstrap4_utilities",
    "djangocms_file",
    "djangocms_icon",
    "djangocms_link",
    "djangocms_picture",
    "djangocms_style",
    "djangocms_snippet",
    "djangocms_googlemap",
    "djangocms_video",
    "djangocms_page_meta",
    "fullurl",
    "compressor",
    "apparatus",
    "debug_toolbar",
]

LANGUAGES = (
    ## Customize this
    ("en", _("English")),
    ("fi", _("Finnish")),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {"code": "en", "name": _("English"),},
        {"code": "fi", "name": _("Finnish"), "public": True,},
    ],
    "default": {"public": True, "hide_untranslated": False, "fallbacks": ["en", "fi"],},
}

CMS_TEMPLATES = (
    ## Customize this
    ("fullwidth.html", _("Fullwidth")),
    ("sidebar_left.html", _("Sidebar Left")),
    ("sidebar_right.html", _("Sidebar Right")),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)
META_SITE_PROTOCOL = "https"
META_USE_SITES = True
META_USE_OG_PROPERTIES = True
META_OG_SECURE_URL_ITEMS = []
META_USE_TWITTER_PROPERTIES = True

COMPRESS_OFFLINE = True
COMPRESS_PRECOMPILERS = [
    ("text/x-scss", "django_libsass.SassCompiler"),
]
if not DEBUG:
    LIBSASS_OUTPUT_STYLE = "compressed"

APPARATUS_DISQUS_SITE = "apparatus-1"
APPARATUS_CODESNIPPET_CDN_BASE_URL = (
    "https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.17.1/build"
)
