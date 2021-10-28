#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dennis Zethof'
SITENAME = 'Dennis Zethof'

SITEURL = 'https://druqtemaker.com'
# SITEURL = 'https://philo-b.xyz/pelican_ceilings'
# SITEURL = 'http://localhost:8000'

# turned it off since it doesn't add anything at
# the moment.
# - Docs say it's only handy in development.
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
DISPLAY_ARTICLE_INFO_ON_INDEX = True  # Shows article date, and more is set so.

MENUITEMS = (
    ('Posts', '/category/posts.html'),
    ('Projects', '/category/projects.html'),
#     ('Music', '/pelican_ceilings/category/music.html'),
    ('Publications', '/pages/publications.html'),
    ('About', '/pages/About.html'),
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
    ('index.html', './images/banners/gg_horizontal_aligned_2c4_cropped.jpg'),
    ('category/posts.html', './images/banners/white_side.jpg'),
    ('category/projects.html', './images/banners/rome.jpg'),
    ('differing-banners.html', './images/banners/red_ceiling.jpg'),
)

# Blogroll
# LINKS = (
#     ('Resume', '#'),
# )

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/dz84'),
	('LinkedIn', 'https://www.linkedin.com/in/denniszethof'),
	('StackOverflow', 'https://stackoverflow.com/users/1726026/dzet'),
    # ('Happycow', 'https://www.happycow.net/members/profile/DZet/'),
	# ('Medium', 'https://medium.com/@denniszethof'),
    # ('Dennis&Roben', 'http://www.dennisenroben.nl'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

