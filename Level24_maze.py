# http://www.pythonchallenge.com/pc/hex/ambiguity.html
__author__ = 'chihchieh.sun'

import urllib.request
from io import BytesIO
from PIL import Image
import zipfile

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
    opener = urllib.request.build_opener(proxy_support, handler)
    return opener

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:41.0) Gecko/20100101 Firefox/41.0",
    "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
}

req = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/maze.png')

for key in headers:
    req.add_header(key, headers[key])

bros = opener('butter', 'fly')
original = Image.open(BytesIO(bros.open(req).read()))
image = original.copy()

width, height = image.size
print('size :%s' %(image.size,))

wall_color = (255, 255, 255, 255)
entrance = ()
out = ()

for i in range(width):
    if image.getpixel((width-1-i,0)) != wall_color:
        entrance = (width-1-i, 0)
        print('Entrance : %r' % (entrance,))
        break

for i in range(width):
    if image.getpixel((i, height-2)) != wall_color:
        out = (i, height-1)
        print('Exit : %r' % (out,))
        break

finded_color = (255, 255, 0, 255)
dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
now = None
new_now = entrance
whole_path = []

while new_now != out:
    now = new_now
    image.putpixel(now, finded_color)

    flag = 0
    for d in dirs:
        x = now[0] + d[0]
        y = now[1] + d[1]
        if width > x >= 0 and height > y >= 0:
            if image.getpixel((x, y)) != wall_color and image.getpixel((x, y)) != finded_color:
                new_now = (x, y)
                flag += 1
                break

    if flag == 0:
        new_now = whole_path.pop()
        image.putpixel(new_now, (255, 0, 255, 255))
        #image.show()
    else:
        whole_path += [now]

whole_path += [new_now]
data = []
for p in whole_path:
    data += [original.getpixel(p)[0]]
    image.putpixel(p, (0, 0, 255, 255))

print('Stop : %r' % (new_now,))
image.show()
image.close()

data = bytearray(data[1::2])
#save
output = open("Level24_solution.zip", "wb")
output.write(data)
output.close()
z = zipfile.ZipFile("Level24_solution.zip")

target = Image.open(z.open('maze.jpg', 'r'))
target.show()
target.close()
z.close()

bros.close()