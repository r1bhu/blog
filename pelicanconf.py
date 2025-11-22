AUTHOR = 'User'
SITENAME = 'Ruminations'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output'

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.png']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.png': {'path': 'favicon.png'},
}

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Theme
THEME = 'themes/minimal-dark'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('GitHub', '#'),
         ('LinkedIn', 'https://www.linkedin.com/in/ribhu-8848/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

import os
import markdown

# Custom Landing Page Content
try:
    with open('content/home.md', 'r', encoding='utf-8') as f:
        md_content = f.read()
        # Skip metadata (simple split by blank line or just parse)
        # For simplicity, we'll just convert the whole thing, but usually we want to strip metadata.
        # Pelican's MarkdownReader is better but complex to invoke here.
        # Let's just assume the user puts content after the metadata block.
        if '\n\n' in md_content:
            _, content = md_content.split('\n\n', 1)
        else:
            content = md_content
        LANDING_PAGE_CONTENT = markdown.markdown(content)
except Exception as e:
    LANDING_PAGE_CONTENT = f"<h1>Welcome</h1><p>Error loading content: {e}</p>"

