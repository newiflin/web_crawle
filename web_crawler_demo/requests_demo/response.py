import requests

print('响应信息')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) Applewebkit/537.36 (KHTML, like Gecko)'
        'Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get('https://www.jianshu.com', headers=headers)
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)
exit() if not response.status_code == requests.codes.ok else print('request sucessfully!')