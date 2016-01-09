#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring with a description"""

__author__ = "子風"
__copyright__ = "Copyright 2015, Sun All rights reserved"
__version__ = "1.0.0"

import urllib.request
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
    return urllib.request.build_opener(proxy_support, handler)


def download(url, username, password):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:41.0) Gecko/20100101 Firefox/41.0",
        "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    }

    req = urllib.request.Request(url, headers=headers)
    bros = opener(username, password)
    data = BytesIO(bros.open(req).read())
    bros.close()

    return data
