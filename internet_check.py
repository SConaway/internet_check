#! /usr/bin/env python3

# Copied from https://stackoverflow.com/a/29854274

import time
import datetime

try:
    import httplib
except:
    import http.client as httplib

last_down = False

def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def date():
    return datetime.datetime.now().strftime("%A, %m/%d/%Y %H:%M:%S")

while True:
    has_internet= have_internet()

    if has_internet:
        if last_down:
            print("Internet just went back online at", date())
            last_down = False

        time.sleep(1)

    else:
        last_down = True
        print("Internet down at", date())
        time.sleep(10)

    #import sys
    #sys.exit()
