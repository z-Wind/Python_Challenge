# http://www.pythonchallenge.com/pc/hex/idiot2.html
__author__ = 'z-Wind'

import urllib.request
import zipfile
from io import BytesIO

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

url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
bros = opener('butter','fly')
response = bros.open(url)
print(response.getheader('Content-Range'))


# for start in range(30203,30314):
#     try:
#         bros.addheaders = [("Range", "bytes=%d-2123456789" % start)]
#         response = bros.open(url)
#         print(start,response.read())
#     except:
#         pass

bros.addheaders = [("Range", "bytes=2123456789-2123456789")]
response = bros.open(url)
print('2123456789',response.read()[::-1])
password = 'invader'[::-1]

# for start in range(2123456789,2123456740,-1):
#     try:
#         bros.addheaders = [("Range", "bytes=%d-2123456789" % start)]
#         response = bros.open(url)
#         print(start,response.read())
#     except:
#         pass

bros.addheaders = [("Range", "bytes=2123456743-2123456789")]
response = bros.open(url)
print('2123456743',response.read())

bros.addheaders = [("Range", "bytes=1152983631-2123456789")]
response = bros.open(url)
content = response.read()
print('1152983631',content)

zobj = BytesIO(content)
z = zipfile.ZipFile(zobj)
z.namelist()
print(z.read('readme.txt',password.encode('utf-8')).decode('utf-8'))
z.extract('package.pack','./Level 21',password.encode())
z.close()
