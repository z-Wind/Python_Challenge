# http://www.pythonchallenge.com/pc/hex/copper.html
__author__ = 'Administrator'

import urllib.request
from io import BytesIO
from PIL import Image,ImageSequence

def opener(username, password):
    # User Name & Password
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = 'http://www.pythonchallenge.com/'
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # Proxy setting
    proxy = urllib.request.getproxies()
    proxy_support = urllib.request.ProxyHandler({'sock5': proxy.get('http')})

    # opener setting
    opener = urllib.request.build_opener(proxy_support,handler)
    return opener

bros = opener('butter','fly')
im = Image.open(BytesIO(bros.open('http://www.pythonchallenge.com/pc/hex/white.gif').read()))
path = [i.getbbox()[0:2] for i in ImageSequence.Iterator(im)]
moves = [(path[i+1][0] - path[i][0], path[i+1][1] - path[i][1]) for i in range(len(path) - 1)]

joy = Image.new(im.mode, (200, 200), 0)
center = (100, 100)
move = (0, 0)
for m in moves:
    joy.putpixel(center, 255)
    if m != (0, 0):
        move = m
    center = (center[0] + move[0], center[1] + move[1])

joy.show()
joy.close()

joy2 = Image.new(im.mode, (200,200), 0)
letter = 0
pos = (30,30)
for p in path:
    if p == (100,100):
        letter += 1
        pos = (letter * 30,) * 2
    else:
        pos = (pos[0] + p[0] - 100, pos[1] + p[1] - 100)
    joy2.putpixel(pos, 255)

joy2.show()
joy.close()