# http://www.pythonchallenge.com/pc/return/italy.html
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


def spiralImg(source):
    target = Image.new(source.mode, (100, 100))
    left, top, right, bottom = (0, 0, 99, 99)
    x, y = 0, 0
    dirx, diry = 1, 0
    h, v = source.size
    for i in range(h * v):
        target.putpixel((x, y), source.getpixel((i, 0)))
        if dirx == 1 and x == right:
            dirx, diry = 0, 1
            top += 1
        elif dirx == -1 and x == left:
            dirx, diry = 0, -1
            bottom -= 1
        elif diry == 1 and y == bottom:
            dirx, diry = -1, 0
            right -= 1
        elif diry == -1 and y == top:
            dirx, diry = 1, 0
            left += 1
        x += dirx
        y += diry
    return target

strip = getImg('http://www.pythonchallenge.com/pc/return/wire.png')
spiral = spiralImg(strip)

# written by me
# spiral = Image.new(strip.mode, (100,100), 0)
# move = [100, 99, 99, 98]
# steps = [1, 1, -1, -1]
# original = [-1, 0]
#
# i = 0
# data = strip.getdata()
# while i < len(data):
#     for direction in range(4):
#         if direction % 2 == 0:
#             for offset in range(move[direction]):
#                 original[0] += steps[direction]
#                 spiral.putpixel(tuple(original), data[i])
#                 i += 1
#
#         else:
#             for offset in range(move[direction]):
#                 original[1] += steps[direction]
#                 spiral.putpixel(tuple(original), data[i])
#                 i += 1
#
#         move[direction] -= 2

spiral.show()
