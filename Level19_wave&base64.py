# http://www.pythonchallenge.com/pc/hex/bin.html:butter:fly
__author__ = 'chihchieh.sun'

import re
import urllib.request
import base64
import wave
import os

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

def hex_bin():
    bros = opener('butter', 'fly')
    page_source = bros.open("http://www.pythonchallenge.com/pc/hex/bin.html").read()
    wav_data = re.findall(r"base64([\s\S]+?)--", page_source.decode('utf-8'))
    indian = open(".\Level19\indian.wav", "wb")
    indian.write(base64.b64decode(wav_data[0].strip('\n')))
    indian.close()

    source = wave.open('.\Level19\indian.wav', 'rb')
    reverse = wave.open('.\Level19\reversed.wav', 'wb')
    reverse.setparams(source.getparams())
    for i in range(source.getnframes()):
        reverse.writeframes(source.readframes(1)[::-1])
    reverse.close()
    source.close()

if not os.path.exists('Level19'):
        os.mkdir('Level19')
hex_bin()