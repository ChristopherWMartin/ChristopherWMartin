# Simple static site generator

## Usage

### Add markdown files

Move markdown files to the `content` directory. If the first line of your file is a timestamp in the format `%Y-%m-%d` (for example: "2020-12-01") it will be treated as that post's publish date. Otherwise timestamps will be generated from the file's last modification date. Posts titles will be automatically parsed from file's first `h1` tag.

Here is an example post:
```markdown
2020-12-01

# Blog post title

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat...
```

### Modify templates

If desired, modify the header, footer, and css files found in the `templates/` directory.

### Update site variables

Change the global variables at the top of `make.py` to reflect your site's URL. 

### Install dependencies & generate site

``` bash
pip3 install -r requirements.txt
python3 make.py
```

All generated files will be placed in the `public/` directory.
