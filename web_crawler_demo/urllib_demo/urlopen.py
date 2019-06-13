import socket
import urllib.request
import urllib.parse
import urllib.error

# ulopen模拟浏览器一个请求
response1 = urllib.request.urlopen("https://www.python.org")
print(type(response1))   # type输出响应的类型
print(response1.status)  # 返回响应状态码
print(response1.getheaders()) # 获取响应头信息
print(response1.getheader('Server'))
print("---------------------------")
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response2 = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response2.read())
print("---------------------------")
response3 = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response3.read())
print("---------------------------")
# 超时请求捕获异常
try:
    response4 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    print(response4.read())
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time Out')