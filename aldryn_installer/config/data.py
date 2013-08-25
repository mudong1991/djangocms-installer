# -*- coding: utf-8 -*-
CONFIGURABLE_OPTIONS = ['--db', '--cms-version', '--django-version', '--i18n',]

DJANGOCMS_DEVELOP = 'https://github.com/divio/django-cms.git@develop#egg=django-cms'
DJANGOCMS_BETA = 'https://github.com/divio/django-cms/archive/3.0.0.beta2.zip'
DJANGOCMS_LATEST = '2.4'

DJANGO_DEVELOP = 'https://github.com/django/django.git@master#egg=django'
DJANGO_BETA = 'https://github.com/django/django/archive/1.6b2.zip'
DJANGO_LATEST = '1.5'


def less_than_version(value):
    items = list(map(int, value.split(".")))
    if len(items) == 1:
        items.append(0)
    items[1] += 1
    return ".".join(map(str, items))


DEFAULT_REQUIREMENTS = """
django-classy-tags>=0.3.4.1
south>=0.7.2
html5lib
django-mptt>=0.5.1,<0.5.3
django-sekizai>=0.7
djangocms-admin-style
djangocms-text-ckeditor>=2.0
git+https://github.com/KristianOellegaard/django-hvad.git#egg=hvad
git+https://github.com/divio/djangocms-column.git#egg=djangocms-column
git+https://github.com/divio/djangocms-style.git#egg=djangocms-style
"""

FILER_REQUIREMENTS = """
easy_thumbnails
django-filer
cmsplugin_filer
"""

PLUGIN_LIST_TEXT = """
aldryn_installer will install and configure the following plugins:
 * djangocms-text-ckeditor (Text plugin)
 * cms.plugins.file (File plugin)
 * cms.plugins.flash (Flash plugin)
 * cms.plugins.googlemap (GoogleMap plugin)
 * cms.plugins.inherit (Inherit plugin)
 * cms.plugins.link (Link plugin)
 * cms.plugins.picture (Picture plugin)
 * cms.plugins.teaser (Teaser plugin)
 * cms.plugins.video (Video plugin)
 * djangocms-style (Style plugin)
                     
It will optionally install cmsplugin-filer plugins (if requested during
configuration):
 * cmsplugin_filer_file (File plugin, replaces cms.plugins.file)
 * cmsplugin_filer_folder (Folder plugin)
 * cmsplugin_filer_image (Image plugin, replaces cms.plugins.picture)
 * cmsplugin_filer_link (Link plugin, replaces cms.plugins.link)
 * cmsplugin_filer_teaser (Teaser plugin, replaces cms.plugins.teaser)
 * cmsplugin_filer_video (Video plugin, replaces cms.plugins.video)
"""

DRIVERS = {
    'django.db.backends.postgresql_psycopg2': 'psycopg2',
    'django.db.backends.postgresql_postgis': 'postgis',
    'django.db.backends.mysql': 'MySQL-python',
    'django.db.backends.sqlite3': '',
}

