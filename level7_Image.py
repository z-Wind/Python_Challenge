#http://www.pythonchallenge.com/pc/def/oxygen.html
__author__ = 'z-Wind'

from PIL import Image
import urllib.request
from io import BytesIO
import  re

# proxy setting
proxy = urllib.request.getproxies()
proxy_support = urllib.request.ProxyHandler({'sock5': proxy.get('http')})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

imgurl = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()
image = Image.open(BytesIO(imgurl))  # Image.open requires a file-like object
imgurl.clse()

w,h = image.size
ans = ''.join([chr(image.getpixel((i, h//2))[0]) for i in range(0, w, 7)])

match = re.findall('\d+',ans)

print(''.join([chr(int(num)) for num in match]))