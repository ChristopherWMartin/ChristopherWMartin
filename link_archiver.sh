#!/bin/bash

# ------------------
# requires:
#   - python3
#   - https://pypi.org/project/markdown-link-extractor
#   - https://github.com/oduwsdl/archivenow
# ------------------

find content/* -type f -name "*.md" | xargs python3 -m markdown_link_extractor | grep -oE '(http|https)://(.*)' |  xargs -L1 archivenow --ia
