from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, \
    ProxyHandler, build_opener
from urllib.error import URLError
import http.cookiejar, urllib.request

# 权限认证
print('1.权限认证')
username = 'username'
password = 'password'
url = 'http://localhost:5000/'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    html = opener.open(url)
    print(html.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

print('2.代理')
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

print('cookie')
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response2 = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name + " = " + item.value)

print('\n')
print('cookie saves in file')
filename1 = 'cookie1.txt'
cookie1 = http.cookiejar.MozillaCookieJar(filename1)
hanler1 = urllib.request.HTTPCookieProcessor(cookie1)
opener1 = urllib.request.build_opener(hanler1)
response1 = opener1.open('https://www.baidu.com')
cookie1.save(ignore_discard=True, ignore_expires=True)

filename2 = 'cookie2.txt'
cookie2 = http.cookiejar.LWPCookieJar(filename2)
handler2 = urllib.request.HTTPCookieProcessor(cookie2)
opener2 = urllib.request.build_opener(handler2)
response2 = opener2.open('https://www.baidu.com')
print(response2.read().decode('utf-8'))
cookie2.save(ignore_discard=True, ignore_expires=True)