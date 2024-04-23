#!/usr/bin/env python

import urllib.request
import urllib.parse

url = "https://i2.ruliweb.com/img/23/03/27/1872050d6154a7eac.jpeg"

savename = 'p291_urldownload.png'

urllib.request.urlretrieve(url, savename)

print('web image : ' + url)
print(savename + 'Saved. . .')