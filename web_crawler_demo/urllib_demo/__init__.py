import urllib.request

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/55.0.2883.87 Safari/537.36'

}
request = urllib.request.Request('https://www.jianshu.com', headers=headers)
response = urllib.request.urlopen(request)
print(response.status)
print(response.read())