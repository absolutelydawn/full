#!/usr/bin/env python

import urllib.request

url = "https://shared-comic.pstatic.net/thumb/webtoon/648419/thumbnail/thumbnail_IMAG10_1421195d-13be-4cde-bcf9-0c78d51c5ea3.jpg"

savename = 'p293_urldownload.png'

result = urllib.request.urlopen(url)

data = result.read()
print('#type(data) : ', type(data))

with open(savename, 'wb') as f:
    f.write(data)
    print(savename + ' Saved. . . . .')