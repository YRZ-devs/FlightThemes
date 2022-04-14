# Loop through all subdirectories (which contain themes)
# and make sure all required files are there.

import os
from pathlib import Path

# CHANGE THIS IF FILES ARE ADDED/REMOVED FROM THE SPEC

folder_structure = {
  "_locales": [
    "messages.json"
  ],
  "css": [
    "dark-theme.css",
    "main.css"
  ],
  "images": [
    "bf_icon_128.ico",
    "bf_icon_128.png",
    "bf_icon.ico",
    "btn-donate.png",
    "cf_logo_black.svg",
    "cf_logo_white.svg",
    "light-wide-1.svg",
    "light-wide-2.svg"
    ]
}

# DO NOT CHANGE BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING 
# (i don't lol)

# get a list of all subdirectories
# ignoring hidden folders, thanks git <3
subfolders = [ f.path for f in os.scandir(os.getcwd()) if f.is_dir() and f.name[0] != "."]

for folder in subfolders:
  print("Found theme in subdirectory {}".format(folder))