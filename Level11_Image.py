# http://www.pythonchallenge.com/pc/return/5808.html
__author__ = 'chihchieh.sun'

from PIL import Image
import urllib.request
from io import BytesIO


def splitOE(source):
    results = []
    width, height = source.size
    results = [Image.new(source.mode, (width//2, height//2))
               for dummy in range(4)]
    for x in range(width):
        for y in range(height):
            target = results[x % 2 + (y % 2 << 1)]
            target.putpixel((x//2, y//2), source.getpixel((x, y)))
    return results

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
#urllib.request.install_opener(opener)

url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
#imUrl = urllib.request.urlopen(url).read()
imUrl = opener.open(url).read()
image = Image.open(BytesIO(imUrl))  # Image.open requires a file-like object
odd_even = splitOE(image)
for result in odd_even:
    result.show()