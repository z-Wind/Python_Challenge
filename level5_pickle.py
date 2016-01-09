#http://www.pythonchallenge.com/pc/def/peak.html
__author__ = 'z-Wind'

# -*- coding: utf-8 -*-

import pickle
# 也可以這樣： C 語言實現版本效率較佳
# import cPickle as pickle
import urllib.request

# proxy setting
proxy = urllib.request.getproxies()
proxy_support = urllib.request.ProxyHandler({'sock5': proxy.get('http')})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

url = r'http://www.pythonchallenge.com/pc/def/banner.p'
req = urllib.request.Request(url)
connect = urllib.request.urlopen(req)
data = pickle.loads(connect.read())
connect.close()

for linelist in data:
    line = [ch * count for ch, count in linelist]
    print("".join(line))
