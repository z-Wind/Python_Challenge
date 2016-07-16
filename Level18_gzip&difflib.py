# http://www.pythonchallenge.com/pc/return/balloons.html
__author__ = 'chihchieh.sun'

from PIL import Image
import urllib.request
from io import BytesIO
import operator
import binascii
import re
import difflib
import gzip

def opener():
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
    return opener

bros = opener()

# nothing, just go to brightness.html
# url = 'http://www.pythonchallenge.com/pc/return/balloons.jpg'
# img = Image.open(BytesIO(bros.open(url).read()))  # Image.open requires a file-like object
#
# h, v = img.size
# diff = Image.new(img.mode, (h, v))
#
# for i in range(h//2):
#     for j in range(v):
#         value = tuple(map(operator.sub, img.getpixel((i, j)), img.getpixel((i + h//2, j))))
#         diff.putpixel((i, j), value)
#
# diff.show()

url = 'http://www.pythonchallenge.com/pc/return/deltas.gz'
data = bros.open(url).read()
content = gzip.GzipFile(fileobj=BytesIO(data)).read().decode('utf-8')
lines = content.split('\n')
pairs = [(l[:53], l[56:]) for l in lines]
part = ['\n'.join([p[i] for p in pairs]) for i in range(2)]


def unhex(s):
    return binascii.unhexlify(re.sub('[^0-9a-fA-F]', '', s))

# wrong image
# for i,data in enumerate(part):
#     open('delta%d.png' % i,'wb').write(unhex(data))

diffs = list(difflib.Differ().compare(part[0].splitlines(), part[1].splitlines()))

pngs = [''.join(filter(lambda l: l[0] == d, diffs)) for d in " +-"]

for i in range(len(pngs)):
    Image.open(BytesIO(unhex(pngs[i]))).show()

