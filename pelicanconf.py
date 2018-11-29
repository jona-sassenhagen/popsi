#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jona Sassenhagen'
SITENAME = "Frankfurt Open Science Initiative"#"POPSI"#'F<br>O<br>P<br>S<br>I<br><br>4<br>E<br>V<br>A'
SITEURL = 'https://jona-sassenhagen.github.io/popsi/'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
#('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),
          ('Open Science Foundation', 'osf.io'),
)

#SITELOGO = '../content/images/goethe.png'

#LACES_SITELOGO = {
#    'file': '../content/images/goethe.png',
#    'width': 100,
#}

BANNER = 'images/goethe.png'
HEADER_COVER = "../content/images/banner.png"
LACES_BANNER = {"file": 'content/images/goethe.png',
"subtitle": "",
"all_pages": True
}

BANNER_SUBTITLE = ''
BANNER_ALL_PAGES = True

#BOOTSTRAP_THEME = 'Lumen'

# Social widget
SOCIAL = (('Open Science Initiative University of Marburg',
'https://openscienceinitiativeuniversitymarburg.github.io'),
("Goethe University Frankfurt", "https://www.goethe-university-frankfurt.de/")
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ['/Users/jona/tools/pelican-plugins/',]
PLUGINS = ['i18n_subsites',]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n'],}

BOOTSTRAP_THEME = 'Spacelab'

#THEME = "/Users/jona/tools/pelican-themes/clean-blog"
#THEME = "/Users/jona/tools/pelican-themes/attila"
#THEME = "/Users/jona/tools/pelican-themes/pelican-bootstrap3"
#THEME = "laces3"
THEME = "blueidea"

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SUBMENU = True

DISPLAY_SEARCH_FORM = True

TYPOGRIFY = True

STATIC_PATHS = ["resources/protocols", "images"]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.tables':{},
    }
}
