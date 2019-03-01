#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dennis Zethof'
SITENAME = 'Dennis Zethof'

SITEURL = 'localhost:8000'

# needed to get siteurl to work, alhough I'm not
# sure how much I really need that.
RELATIVE_URLS = True 

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

THEME = './theme/pelican-bootstrap3-custom'
BOOTSTRAP_THEME = 'flatly'

##################################################
''' PLUGIN NOTES:

    pelican_javascript: 
        - makes use of content/css and content/js, 
        subfolders don't seem to work.
        - I don't know whether this plugin or
        pelican transfers all files content/css
        to output, but in any case I don't have to
        do that manually (via STATIC_PATHS and 
        EXTRA_PATH_METADATA).
'''
PLUGIN_PATHS = ['./plugins', ]
PLUGINS = [
    'i18n_subsites',
    'pelican_javascript',
    'jinja2content',
]

# seems the i18n extension has to be included
# in order for the pelican-bootstrap3 framework
# to work.
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
JINJA2CONTENT_TEMPLATES = ['templates/includes']

CUSTOM_CSS = 'css/custom.css'

#     'css',
#   ]
# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'static/custom.css'},
#     'css/nutty-mind.css': {'path': 'static/nutty-mind.css'}
#   }


# attempt to solve error
# READERS = {'html': None}
# STATIC_PATHS = ['templates/includes']
# PAGE_EXCLUDES = ['templates/includes/nutty-mind.html']
# ARTICLE_EXCLUDES = ['templates/includes/nutty-mind.html']

# ARTICLE_ORDER_BY = 'date'
# PAGE_ORDER_BY = 'sortorder' 
# PAGES_SORT_ATTRIBUTE = 'sortorder'
# REVERSE_CATEGORY_ORDER = False
# NEWEST_FIRST_ARCHIVES = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Projects', '/category/projects.html'),
    ('Music', '/category/music.html'),
    ('Publications', '/pages/publications.html'),
    ('About', '/pages/About.html'),
)

DISQUS_SITENAME = 'site-ceilings'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# link has to point for resulting situation in output
BANNER = './images/gg_horizontal.jpg'
# BANNER_SUBTITLE = 'THE subtitles'
BANNER_ALL_PAGES = False

# Blogroll
# LINKS = (
#     ('aother link', '#'),
# )

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/dzet'),
    ('LinkedIn', 'https://www.linkedin.com/in/denniszethof'),
    ('Happycow', 'https://www.happycow.net/members/profile/DZet/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

