import os
from collections import OrderedDict
import time
from datetime import datetime
from shutil import copyfile, copytree, rmtree
import dateutil
import pytz
import markdown2
from feedgen.feed import FeedGenerator

URL = "https://chriswmartin.github.io"
SITE_NAME = "Textfile"
AUTHER_NAME = "Chris Martin"
AUTHOR_EMAIL = "chrismartin@riseup.net"

MARKDOWN_DIR = "content"
PUBLIC_DIR = "."
POST_DIR = PUBLIC_DIR + "/posts"
MD_MEDIA_DIR = MARKDOWN_DIR + "/media"
PUBLIC_MEDIA_DIR = POST_DIR + "/media"

TEMPLATE_DIR = "templates"
HEAD_TEMPLATE = TEMPLATE_DIR + "/head.html"
HEADER_TEMPLATE = TEMPLATE_DIR + "/header.html"
FOOT_TEMPLATE = TEMPLATE_DIR + "/foot.html"
FOOTER_TEMPLATE = TEMPLATE_DIR + "/footer.html"
GLOBAL_CSS_TEMPLATE = TEMPLATE_DIR + "/styles.css"

# -------------------------
# set up rss / atom feeds
# -------------------------
fg = FeedGenerator()
fg.id(URL)
fg.title(SITE_NAME)
fg.author({'name': AUTHER_NAME,'email': AUTHOR_EMAIL})
fg.description('A blog by' + ' ' + AUTHER_NAME)
fg.link(href=URL, rel='alternate')
fg.link(href=URL + '/feed.atom', rel='self')
fg.language('en')

# --------------------------------------------------------------
# sort all markdown files by creation date (most recent first)
# --------------------------------------------------------------
def create_sorted_post_dict(post_dir):
    posts = {}
    filepaths = [os.path.join(post_dir, file) for file in os.listdir(post_dir) if file.endswith(".md")]
    for file in filepaths:
        with open(file, "r") as f:

            for line in f:
                if line[0] == "#":
                    title = line.strip("#").lstrip()
                    break

            f.seek(0)
            first_line = f.readline().strip('\n')
            try:
                dateutil.parser.parse(first_line, fuzzy=True)
                date = first_line
            except ValueError:
                timestamp =  time.ctime(os.path.getmtime(file))
                date = datetime.strptime(str(timestamp), "%a %b %d %H:%M:%S %Y").strftime('%Y-%m-%d')

        d = {file: { "title": title, "date": date}}
        posts.update(d)
    sorted_dict = dict(OrderedDict(sorted(posts.items(), key=lambda t:t[1]["date"], reverse=True)))
    return sorted_dict
posts = create_sorted_post_dict(MARKDOWN_DIR)

# ----------------------------------------------
# assemble post & index html from markdown & templates
# ----------------------------------------------
posts_ul = ""
for post in posts:
    with open(post) as f:
        title = posts[post]['title']
    timestamp = posts[post]['date']
    
    top_data = ""
    for file in [HEAD_TEMPLATE, HEADER_TEMPLATE]:
        with open(file, 'r') as html:
            data = html.read()
        top_data += data
    
    bottom_data = ""
    for file in [FOOTER_TEMPLATE, FOOT_TEMPLATE]:
        with open(file, 'r') as html:
            data = html.read()
        bottom_data += data
     
    posts_ul += "<li><a href=posts/" + post.split("/")[1].split(".")[0] + ".html>" + title + "</a><small class='timestamp'><" + timestamp + "></small></li>" 

    post_html = markdown2.markdown_path(post, extras=["fenced-code-blocks"])
    assembled_post_html = top_data + post_html + bottom_data
    with open(POST_DIR + "/" + post.split("/")[1].split(".")[0] + ".html", 'w') as assembled_post:
        assembled_post.write(assembled_post_html)

    # ------------------------------
    # add post to rss / atom feeds
    # ------------------------------
    date_time_obj = datetime.strptime(posts[post]['date'], '%Y-%m-%d')
    timezone = pytz.timezone('America/New_York')
    localized_timestamp = timezone.localize(date_time_obj)
    fe = fg.add_entry()
    fe.id(URL + "/" + POST_DIR + "/" + post.split("/")[1].split(".")[0] + ".html")
    fe.title(posts[post]['title'])
    fe.description('A blog post by' + ' ' + AUTHER_NAME)
    fe.link({'href': URL + "/" + POST_DIR + "/" + post.split("/")[1].split(".")[0] + ".html", 'rel': 'alternate'})
    fe.published(localized_timestamp)
    fe.updated(localized_timestamp)

# --------------------------
# save index.html file
# --------------------------
assembled_index_html = top_data + "<ul>" + posts_ul + "</ul>" + bottom_data
with open(PUBLIC_DIR + "/" + "index.html", 'w') as index:
    index.write(assembled_index_html)

# -----------------------------------------------
# copy media directory to public post directory
# -----------------------------------------------
if os.path.exists(PUBLIC_MEDIA_DIR):
    rmtree(PUBLIC_MEDIA_DIR)
copytree(MD_MEDIA_DIR, PUBLIC_MEDIA_DIR)

# ------------------------------------------------------------
# copy css files from template directory to public directory
# ------------------------------------------------------------
copyfile(GLOBAL_CSS_TEMPLATE, PUBLIC_DIR + "/styles.css")
copyfile("templates/pygments/pastie.css", PUBLIC_DIR + "/pastie.css")
copyfile("templates/pygments/monokai.css", PUBLIC_DIR + "/monokai.css")

# -----------------------
# save rss / atom files
# -----------------------
fg.atom_file(PUBLIC_DIR + '/atom.xml')
fg.rss_file(PUBLIC_DIR + '/rss.xml')
