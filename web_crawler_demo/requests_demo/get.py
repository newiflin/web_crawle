import requests
import re

# Get请求
print('访问百度')
response = requests.get('https://www.baidu.com')
print(response.status_code)
print(type(response))
print(type(response.text))
print(response.text)
print(response.cookies)

print('访问httpbin')
data = {
    'name': 'Ben',
    'age': 22
}
response = requests.get('http://httpbin.org/get', params=data)
print(response.text)
print(response.json())
print(type(response.json()))

print('\n抓取知乎网页')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) Applewebkit/537.36 (KHTML, like Gecko)'
        'Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get('https://www.zhihu.com/explore', headers=headers);
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, response.text)
print(titles)

print('\n抓取github图片')
response = requests.get('https://github.com/favicon.ico')
print(response.text)
print(response.content)
with open('favicon.ico', 'wb') as f:
    f.write(response.content)