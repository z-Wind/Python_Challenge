# http://www.pythonchallenge.com/pc/def/linkedlist.php
__author__ = 'z-Wind'

import urllib.request
import urllib.error
import re

# proxy setting
proxy = urllib.request.getproxies()
proxy_support = urllib.request.ProxyHandler({'sock5': proxy.get('http')})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)


urls = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
end = '63579'#'8022'#'12345'

while end != '':
    print(urls+end)
    req = urllib.request.Request(urls+end)

    try:
        connect = urllib.request.urlopen(req)
        content = connect.read().decode("utf-8")
        connect.close()
        print(content)
        match = re.search(r' (\d+)$',content)

        if match:
            end = match.group(1)
        else:
            break
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())


