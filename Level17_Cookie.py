# http://www.pythonchallenge.com/pc/return/romance.html
__author__ = 'z-Wind'

import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
import re
import bz2
import xmlrpc.client


def unquote_plus_to_bytes(s):
    if isinstance(s, bytes):
        s = s.replace(b'+', b' ')
    else:
        s = s.replace('+', ' ')
    return urllib.parse.unquote_to_bytes(s)


def getcookies(url):
    # User Name & Password
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = 'http://www.pythonchallenge.com/pc/return/'
    password_mgr.add_password(None, top_level_url, 'huge', 'file')
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # Proxy setting
    proxy = urllib.request.getproxies()
    proxy_support = urllib.request.ProxyHandler({'sock5': proxy.get('http')})

    # cookies
    cookies = http.cookiejar.CookieJar()
    cookies_header = urllib.request.HTTPCookieProcessor(cookies)

    # opener setting
    opener = urllib.request.build_opener(proxy_support, handler, cookies_header)
    return opener.open(url), cookies


connect, cookies = getcookies('http://www.pythonchallenge.com/pc/def/linkedlist.php')
for cookie in cookies:
    print(cookie.name, cookie.value)

urls = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
end = '12345'
message = []

while end != '':
    # print(urls+end)

    try:
        connect, cookies = getcookies(urls + end)
        message.append(list(cookies)[0].value)

        content = connect.read().decode("utf-8")
        connect.close()
        # print(content)
        match = re.search(r' (\d+)$', content)

        if match:
            end = match.group(1)
        else:
            break
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())

info = ''.join(message)
print(info)

print('%s' % bz2.decompress(unquote_plus_to_bytes(info)).decode("utf-8"))

# Mozart's birthe day and find his father Leopold

phonebook = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(phonebook.phone('Leopold').lower())


# User Name & Password
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = 'http://www.pythonchallenge.com/pc/return/'
password_mgr.add_password(None, top_level_url, 'huge', 'file')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# Proxy setting
proxy = urllib.request.getproxies()
proxy_support = urllib.request.ProxyHandler({'sock5': proxy.get('http')})

# opener setting
opener = urllib.request.build_opener(proxy_support, handler)

uri = "http://www.pythonchallenge.com/pc/stuff/violin.php"
msg = "the flowers are on their way"
req = urllib.request.Request(uri, headers={"Cookie": "info=" + urllib.parse.quote_plus(msg)})
print(opener.open(req).read())
