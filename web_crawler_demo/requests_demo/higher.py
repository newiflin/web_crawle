import requests
import logging
from requests.auth import HTTPBasicAuth
from requests import Request, Session

# requests高级用法
print('1.上传文件')
files = {'file': open('favicon.ico', 'rb')}
response = requests.post('http://httpbin.org/post', files=files)
print(response.text)

print('2.设置Cookie')
print('2.1.获取Cookie')
response = requests.get('https://www.baidu.com')
print(response.cookies)
for key,value in response.cookies.items():
    print(key + '=' + value)

print('2.2.通过Cookie登录知乎')
headers = {
    'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Host': 'www.zhihu.com'
}
Cookies = '_zap=d0ca9f5b-6f1c-4ee3-ae3e-de93c5388310; d_c0="ACDioy6c_w6PTh2jh_XtiBKoD_dk97UqeGw=' \
          '|1550451871"; z_c0="2|1:0|10:1550451929|4:z_c0|92:Mi4xRlVNYkF3QUFBQUFBSU9Lakxwel9EaVlB' \
          'QUFCZ0FsVk4yVkpYWFFDQUp5Y3lDWlZ5b1dPM0s5eUF3WkVTT0h4eDlR|de6f8ccad6602204c212c7252a5c3' \
          'a9c8688b87099b8aa6daea9b863d5bc1cdb"; tst=r; __utmv=51854390.100--|2=registration_date' \
          '=20160603=1^3=entry_date=20160603=1; __utma=51854390.632586640.1552203502.1552203502.1' \
          '552271761.2; __utmz=51854390.1552271761.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=' \
          'referral|utmcct=/search; _xsrf=C33cu9dQUU13zxwMgkJ4Fzjcf0wlnB1u; __gads=ID=a1072b4ee08' \
          'f7d60:T=1554390891:S=ALNI_MaUgy5WqCot-D0gQXjaHFpfYChIPQ; q_c1=d6af09ab6dc1476887ca7211' \
          '6ce2786d|1559093376000|1550451933000; tgw_l7_route=f2979fdd289e2265b2f12e4f4a478330'
jar = requests.cookies.RequestsCookieJar()
for cookie in Cookies.split(","):
    key, value = cookie.split('=', 1)
    jar.set(key, value)
response = requests.get('https://www.zhihu.com', headers=headers, cookies=jar)
print(response.text)

print('\n3.会话的维持')
# response = requests.get('https://httpbin/org/cookies/set/number/123456789')
# r = requests.get('https://httpbin/org/cookies')
# print(r.text)
#
# s = requests.session()
# s.get('https://httpbin/org/cookies/set/number/123456789')
# r = s.get('https://httpbin/org/cookies')
# print(r.text)

print('\n4.SSL证书验证')
logging.captureWarnings(True)
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

print('\n5.代理')
proxies = {
    'http': 'http://120.76.58.229:3128',
    'https': 'https://120.76.58.229:1080'
}
requests.get('https://www.taobao.com', proxies=proxies)

print('\n6.超时设置')
response = requests.get('https://www.taobao.com', timeout = 1)
print(response.status_code)

print('\n7.身份认证')
response = requests.get('http://localhost:500', auth=HTTPBasicAuth('username', 'password'))
print(requests.status_codes)

print('\n8.Prepared Request')
url = 'http://httpbin.org/post'
data = {
    'name:': 'germey'
}
headers={
    'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
s = Session()
resquest = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(resquest)
response = s.send(prepped)
print(response.status_code)