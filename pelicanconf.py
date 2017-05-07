#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import path

AUTHOR = u'Hypatia'
SITENAME = u'Transmisogyny'
SITEURL = 'transmisogyny.info'
THEME = path.join(path.dirname(__file__), 'iridescent')
print(THEME)

PATH = 'content'

COPYRIGHT_TEXT = u'Transmisogyny.info - Hypatia Software Organization &#169;'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_AUTHOR = None

SITE_IMAGE = u'images/logo.png'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# MENUITEMS = (("Testimony", "%s/blog.html" % SITEURL),)

DEFAULT_PAGINATION = 10

INDEX_SAVE_AS = "blog.html"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
