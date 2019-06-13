import urllib.request
import urllib.parse

print('1.----------------')
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

print('2.----------------')
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'LiHua'
}
data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
request1 = urllib.request.Request(url, data=data, headers=headers, method='POST')
response2 = urllib.request.urlopen(request1)
print(response2.read().decode('utf-8'))
