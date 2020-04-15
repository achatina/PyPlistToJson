#!/usr/bin/env python
import json
import plistlib
import glob
import os


def parse_files():
    files = [f for f in glob.glob("**/*.plist", recursive=True)]
    print(files)
    for f in files:
        with open(f, "rb") as file:
            plist_dict = plistlib.load(file)
            result = json.dumps(plist_dict)
            filename = os.path.basename(file.name)
            pre, ext = os.path.splitext(filename)
            jsonfile = open(pre + ".json", "w")
            jsonfile.write(result)
            jsonfile.close()
            print(jsonfile)


if __name__ == '__main__':
    parse_files()
