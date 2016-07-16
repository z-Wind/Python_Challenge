#http://www.pythonchallenge.com/pc/def/channel.html
__author__ = 'chihchieh.sun'

import re
import urllib.request
import zipfile
from io import BytesIO

# proxy setting
proxy = urllib.request.getproxies()
proxy_support = urllib.request.ProxyHandler({'sock5': proxy.get('http')})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

zobj = BytesIO()
zobj.write(urllib.request.urlopen("http://pythonchallenge.com/pc/def/channel.zip").read())
z = zipfile.ZipFile(zobj)

#pre_path = r'./level6 list/'
file_name = '90052'
order = [file_name]

while True:
    print('%s.txt' %(file_name))
    target = z.open(file_name + '.txt','r')
    content = target.read().decode('utf-8')
    target.close()
    print(content)
    match = re.search(r' (\d+)$',content)

    if match:
        file_name = match.group(1)
        order.append(file_name)
    else:
        break

#z = zipfile.ZipFile(pre_path + 'channel.zip')
comment = [z.getinfo('%s.txt' %name).comment for name in order]
print(''.join(str.decode('utf-8') for str in comment))
z.close()
