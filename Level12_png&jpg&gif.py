# http://www.pythonchallenge.com/pc/return/evil.html
__author__ = 'z-Wind'

import urllib.request
import  os
from PIL import Image
from io import BytesIO

# User Name & Password
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = 'http://www.pythonchallenge.com/pc/return/'
password_mgr.add_password(None, top_level_url, 'huge', 'file')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# Proxy setting
proxy = urllib.request.getproxies()
proxy_support = urllib.request.ProxyHandler({'sock5': proxy.get('http')})

# opener setting
opener = urllib.request.build_opener(proxy_support, handler)

print(opener.open('http://www.pythonchallenge.com/pc/return/evil4.jpg').read())

url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
gfx = opener.open(url).read()

if not os.path.exists('Level12'):
    os.mkdir('Level12')
types = ['jpg', 'png', 'gif', 'png', 'jpg']
for i in range(5):
    im = Image.open(BytesIO(gfx[i::5]))
    f = open('.\Level12\evil2_%d.%s' % (i, im.format.lower()), 'wb')
    f.write(gfx[i::5])
    f.close()
