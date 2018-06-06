# -*- coding: utf-8 -*-

import time

BLOG_AUTHOR = u"Mike"
BLOG_TITLE = u"Raspberry VI"
BLOG_DESCRIPTION = u"Raspberry Pi hacking for the visually-impaired"

SITE_URL = u"http://www.raspberryvi.org/"
BLOG_EMAIL = u"mike@raspberryvi.org"

DEFAULT_LANG = "en"


NAVIGATION_LINKS = {
    DEFAULT_LANG: (
	("/stories/index.html", "Home"),
        ("/stories/about.html", "About"),
	(
		(
			('/stories/general.html', 'General'),
			('/stories/arduino.html', 'Arduino'),
			('/stories/beagle.html','Beaglebone'),
			('/stories/raspberry-pi.html','Raspberry Pi'),
		), 
'Pages'
	),
	("/stories/reference.html", "Reference"),
	("/stories/links.html", "Links"),
	("/mike/index.html", "Blog"),
	("/stories/downloads.html", "Downloads"),
        ("/archive.html", "Archive"),
        ("/categories/index.html", "Tags"),
        ("/rss.xml", "RSS feed"),
    ),
}



THEME = "mybase"



POSTS = (
	("posts/*.md", "posts", "post.tmpl"),
	("posts/*.kd", "posts", "post.tmpl"),
	("posts/*.rst", "posts", "post.tmpl"),
	("posts/*.org", "posts", "post.tmpl"),
	("posts/*.t2t", "posts", "post.tmpl"),
	("posts/*.txt", "posts", "post.tmpl"),
	("posts/*.php", "posts", "post.tmpl"),
)

PAGES = (
	("stories/*.md", "stories", "story.tmpl"),
	("stories/*.kd", "stories", "story.tmpl"),
	("stories/*.rst", "stories", "story.tmpl"),
	("stories/*.org", "stories", "story.tmpl"),
	("stories/*.t2t", "stories", "story.tmpl"),
	("stories/*.txt", "stories", "story.tmpl"),
	("stories/*.php", "stories", "story.tmpl"),
)

COMPILERS = {
	"markdown": ('.md', '.mdown', '.markdown',),
	"kramdown": ('.kd', '.kdown', '.kramdown',),
	"orgmode": ('.org',),
	"rest": ('.rst', '.txt',),
	"textile": ('.textile',),
	"txt2tags": ('.t2t',),
	"bbcode": ('.bb',),
	"wiki": ('.wiki',),
	"ipynb": ('.ipynb',),
	"html": ('.html', '.htm'),
	# PHP files are rendered the usual way (i.e. with the full templates).
	# The resulting files have .php extensions, making it possible to run
	# them without reconfiguring your server to recognize them.
	"php": ('.php',),
	# Pandoc detects the input from the source filename
	# but is disabled by default as it would conflict
	# with many of the others.
	# "pandoc": ('.rst', '.md', '.txt'),
}

LOGO_URL = "/images/linux_rasp_dog_4.gif"
SHOW_BLOG_TITLE = True
WRITE_TAG_CLOUD = True

INDEX_PATH = "mike"

URL_TYPE = "rel_path"
USE_BASE_TAG = False


REDIRECTIONS = []


DEPLOY_COMMANDS = {
    'default': [
	"touch temp~",
	"rm *~",
        "find . -name *~ -exec rm {} \;",
        "rsync --exclude-from=exclude-from-rsync -rav --delete output/ /var/www/html",
    ],
    'intruder': [
	"touch temp~",
	"rm *~",
        "find . -name *~ -exec rm {} \;",
        "rsync --exclude-from=exclude-from-rsync -rav --delete output/ /var/www/html",
        "rsync -rav --delete twigtemplates/ /var/www:twigtemplates",
        "rsync -rav --delete php/ /var/www:php"
    ],
    'live': [
	"touch temp~",
	"rm *~",
        "find . -name *~ -exec rm {} \;",
        "rsync --exclude-from=exclude-from-rsync -rav --delete output/ raspberryvi.org@raspberryvi.org:public_html",
        "rsync -rav --delete twigtemplates/ raspberryvi.org@raspberryvi.org:twigtemplates",
        "rsync -rav --delete php/ raspberryvi.org@raspberryvi.org:php"
    ],

    }



INDEX_TEASERS = True

INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

PATRONS = """
<p>Hosted by <a href="http://www.falcoda.com">falcoda.com</a></p>
"""




DISCLAIMER = """
<p>
Raspberry VI is not connected with, or affiliated to
<a href="http://www.raspberrypi.org/">The Raspberry Pi Foundation</a>.
  Any opinions, practices or products mentioned
herein are not endorsed by the Foundation.
</p>
"""


LICENSE = """
<a rel="license">
<p>Unless otherwise stated all content released under the
<a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
<img alt="Creative Commons License BY-NC-SA" style="border-width:0; margin-bottom:0px;" src="http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png">
</a>
</p>
"""

CONTENT_FOOTER = """
<hr>
{disclaimer}<br>
Site last updated: {date} by
        <a href="mailto:{email}">{author}</a><br>
Powered by <a href="http://getnikola.com" rel="nofollow">Nikola</a><br>
         {license}
<!-- <br> -->
{patrons}
"""

CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.strftime("%Y-%m-%d %H:%M", time.gmtime()),
             "patrons": PATRONS,
            "license": LICENSE,
            "disclaimer": DISCLAIMER
        }
    )
}

COMMENT_SYSTEM = ""
COMMENT_SYSTEM_ID = ""

MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite', 'extra', 'markdown_include.include']

SHOW_SOURCELINK = False

COPY_SOURCES = False

UNSLUGIFY_TITLES = True

