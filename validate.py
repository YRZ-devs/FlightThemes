# Loop through all subdirectories (which contain themes)
# and make sure all required files are there.

import os
from pathlib import Path
import sys

# CHANGE THIS IF FILES ARE ADDED/REMOVED FROM THE SPEC
# this is very quickly thrown together. will rewrite with proper
# support for subdirectories but for now it just needs to work

schema = {
    "_locales/en": ["messages.json"],
    "css": ["dark-theme.css", "main.css"],
    "images": [
        "bf_icon_128.ico",
        "bf_icon_128.png",
        "bf_icon.ico",
        "btn-donate.png",
        "cf_logo_black.svg",
        "cf_logo_white.svg",
        "light-wide-1.svg",
        "light-wide-2.svg",
    ],
}

# DO NOT CHANGE BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING
# (i don't lol)

# get a list of all subdirectories
# ignoring hidden folders, thanks git <3
subfolders = [
    f.path for f in os.scandir(os.getcwd()) if f.is_dir() and f.name[0] != "."
]

# variable to keep track of missing files, for logging purposes
missing_files = []

for cwd_folder in subfolders:
    current_theme = cwd_folder.replace("\\", "/").split("/")[-1]
    cwd = Path(cwd_folder)
    for schema_folder in schema:
        folder = Path(cwd, schema_folder)
        if folder.exists():
            # Folder exists, check for all files within
            for schema_file in schema[schema_folder]:
                file = Path(folder, schema_file)
                if not file.exists():
                    missing_files.append("{}/{}/{}".format(current_theme, schema_folder, schema_file))
        else:
            # Folder does not exist, add to missing files
            missing_files.append("{}/{}".format(current_theme, schema_folder))


# Check if any of the files were actually missing
if len(missing_files) > 0:
    # If so, pretty-print the missing files
    print("The following files are missing:")
    print("\n".join(missing_files))
    sys.exit(1)
else:
    # LETS GOOOOOOOO
    print("Themes look all good!")
    sys.exit(0)
