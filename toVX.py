import time
import sys
import os
import re
sys.path.append(os.path.abspath("SO_site-packages"))

import pyperclip

recent_value = ""
regex1 = "^https?:\/\/twitter\.com\/(?:#!\/)?(\w+)\/status(es)?\/(\d+)"
regex2 = "^https?:\/\/vxtwitter\.com\/(?:#!\/)?(\w+)\/status(es)?\/(\d+)"

while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        if re.search(regex1, recent_value):
            newurl = re.sub('twitter', 'vxtwitter', recent_value)
            pyperclip.copy(newurl)
            print("converted to vxtwitter and copied to clipboard\n")
        elif re.search(regex2, recent_value):
            print("waiting for new twitter link\n")
        else:
            print("not a twitter link\n")
            

    time.sleep(0.1)
