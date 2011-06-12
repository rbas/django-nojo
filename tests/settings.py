# coding: utf-8

DEFAULT_CHARSET = 'utf-8'

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'

ROOT_URLCONF = 'settings'

SITE_ID = 1

INSTALLED_APPS = (
    'nojo',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.load_template_source',
)
