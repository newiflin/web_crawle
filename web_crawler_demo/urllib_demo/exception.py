from urllib import request, error
import socket

# 打开一个不存在的页面
print('URLError')
try:
    response1 = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)
print('\n')
print('HTTPError')
try:
    response2 = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers)
except error.URLError as e:
    print(e.reason)
else:
    print('Request Sucessfully')

print('\n')
print('timeout')
try:
    response3 = request.urlopen('https://www.baidu.com', timeout=0.01)
except error.URLError as e:
    print(type(e.reason))
    if (isinstance(e.reason, socket.timeout)):
        print('Time Out')