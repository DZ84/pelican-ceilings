#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dennis Zethof'
SITENAME = 'Dennis Zethof'

# SITEURL = 'https://philo-b.xyz/pelican_ceilings'
SITEURL = 'http://localhost:8000'

# turned it off since it doesn't add anything at
# the moment.
# RELATIVE_URLS = True

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

DISQUS_SITENAME = 'site-ceilings'
# DISQUS_SITENAME = 'philo-b.xyz'
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-135283341-1'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'auto' 

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Posts', '/pelican_ceilings/category/posts.html'),
    ('Projects', '/pelican_ceilings/category/projects.html'),
#     ('Music', '/pelican_ceilings/category/music.html'),
    ('Publications', '/pelican_ceilings/pages/publications.html'),
    ('About', '/pelican_ceilings/pages/About.html'),
)

'''
made absolete by adjustments:
    BANNER
    BANNER_ALL_PAGES

    perhaps in the future:
    BANNER_SUBTITLE
'''

CUSTOM_BANNERS = (
    # ('index', './images/banners/gg_horizontal_aligned_1.jpg'),
    ('index', './images/banners/gg_horizontal_aligned_2c4_cropped.jpg'),
    ('category/posts', './images/banners/white_side.jpg'),
    ('category/projects', './images/banners/rome.jpg'),
)

# Blogroll
# LINKS = (
#     ('Resume', '#'),
# )

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/dzet'),
    ('LinkedIn', 'https://www.linkedin.com/in/denniszethof'),
    ('Happycow', 'https://www.happycow.net/members/profile/DZet/'),
    ('Dennis&Roben', 'http://www.dennisenroben.nl'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

