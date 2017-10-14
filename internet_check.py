#! /usr/bin/env python3

# Copied from https://stackoverflow.com/a/29854274

import time
import datetime

try:
    import httplib
except:
    import http.client as httplib



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

def minute():
    return int(datetime.datetime.now().strftime("%M"))


last_down = False

while True:
    if have_internet():
        last_uptime = minute()
        break


while True:
    has_internet= have_internet()

    if has_internet:
        if last_down:
            print("Internet just went back online at", date())
            last_down = False
            last_uptime = minute()


        time.sleep(1)

    else:
        last_down = True
        print("Internet down at", date())
        time.sleep(10)

    #import sys
    #sys.exit()
