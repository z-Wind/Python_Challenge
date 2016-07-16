# http://www.pythonchallenge.com/pc/return/mozart.html
__author__ = 'chihchieh.sun'

from PIL import Image
import urllib.request
from io import BytesIO


def getImg(url):
    # User Name & Password
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = 'http://www.pythonchallenge.com/pc/return/'
    password_mgr.add_password(None, top_level_url, 'huge', 'file')
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # Proxy setting
    proxy = urllib.request.getproxies()
    proxy_support = urllib.request.ProxyHandler({'sock5': proxy.get('http')})

    # opener setting
    opener = urllib.request.build_opener(proxy_support,handler)
    imUrl = opener.open(url).read()
    return Image.open(BytesIO(imUrl))  # Image.open requires a file-like object

img = getImg('http://www.pythonchallenge.com/pc/return/mozart.gif')

h, v = img.size
bars = []

# find color
count, target, temp = 0, 0, 0
for i in range(h):
    color = img.getpixel((i,0))
    if color == temp:
        count += 1
        if count == 4:
            target = temp
            print('color :', target)
    else:
        count = 0

    temp = color

# redraw
shift = Image.new(img.mode, (h, v))
for j in range(v):
    colors = [img.getpixel((x,j)) for x in range(h)]
    start = colors.index(target) - 1
    colors = colors[start:] + colors[:start]
    for i in range(h):
        shift.putpixel((i, j), colors[i])

shift.putpalette(img.getpalette())
shift.show()
