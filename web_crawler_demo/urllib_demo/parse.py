from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin, \
urlencode, parse_qs, quote, unquote

# urlparse 识别和分段url
result1 = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(type(result1), result1)
print(result1.scheme, result1[0], result1.netloc, result1[1])
# ParseResult是一个元组，可以通过索引或属性名获取

# urlunparse 合并url
print()
data1 = ['http', 'www.baidu.com', 'index.html', 'user', 'id=5', 'comment']
print(urlunparse(data1))

# urlsplit 少了param部分
print()
result2 = urlsplit('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(type(result2), result2)
print(result2[0], result2.scheme)

# urlunsplit 合并url，参数必须为5个
print()
data2 = ['http', 'www.baidu.com', 'index.html', 'id=5', 'comment']
print(urlunsplit(data2))

# urljoin() 生成url，第一个参数base_url，第二个参数缺失(scheme,netloc或path)就按base_url部分补充
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))

# urlencode 将字典类型转换get请求参数
print()
param = {
    'name': 'XiaoMing',
    'age': 12
}
base_url = 'http://www.baidu.com'
url = base_url + urlencode(param)
print(url)

# parse_qs将get请求参数转换为字典类型
query = 'name=Lee&age=22'
print(parse_qs(query))

# quote() 可以将内容转换为URL编码的格式
print()
keyword = '壁纸'
url = 'http://www.baidu.com/s?wd=' + quote(keyword)
print(url)

# unquote() 解析URL编码
print()
print(unquote(url))




