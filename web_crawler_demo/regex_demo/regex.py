import re

print('1.match')
content = 'Hello 123 4567 world_this is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

print('\n2.匹配目标')
content = 'Hello 1234567 world_this is a Regex Demo'
result = re.match('^Hello\s(\d+)\sworld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())

print('\n3.通用匹配')
content = 'Hello 123 4567 world_this is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())

print('\n4.贪婪与非贪婪')
content = 'Hello 1234567 world_this is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content) #.*会尽可能的匹配字符
print(result)
print(result.group(1))
result = re.match('^He.*?(\d+).*Demo$', content) #.*?会尽可能少的匹配字符
print(result)
print(result.group(1))

content = 'https://webo.com/comment/ending'
result1 = re.match('^https://.*?', content) #如果字符串在结尾， .*?可能什么都不匹配
result2 = re.match('^https://.*', content)
print(result1)
print(result2)

print('\n5.修饰符')
content = '''Hello 1234567 World_This 
is a Regex Demo'''
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))

print('\n6.转义匹配')
content = '(百度)www.baidu.com'
result = re.match('\(百度\).*\..*\..*', content)
print(result)

print('\n7.Search')
content = 'Extra strings Hello 1234567 world_this is a Regex Demo'
result = re.match('He.*(\d+).*Demo$', content)
print(result)
result = re.search('He.*(\d+).*Demo$', content)
print(result)

html = '''<div id='song_list'>
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href='/2.mp3' singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href='/3.mp3' singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
'''
result = re.search('li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result.group(1), result.group(2))
result = re.search('li.*?singer="(.*?)">(.*?)</a>', html, re.S)  #返回匹配到的第一个
print(result.group(1), result.group(2))
result = re.search('li.*?singer="(.*?)">(.*?)</a>', html)  #返回未换行<li> 匹配到的第一个
print(result.group(1), result.group(2))

print('\n8.findall()')
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0], result[1], result[2])

print('\n8.sub')
results = re.findall('<li.*?>\s*?(<a.*?>)(\w+)(</a>)?\s*?</li>', html, re.S)
print(results)
for result in results:
    print(result[1])
html = re.sub('<a.*?>|</a>|\n', '', html)  #去掉a标签和换行
print(html)
results = re.findall('<li.*?>(.*?)</li>', html, re.S)
print(results)
for result in results:
    print(result)

print('\n9.compile()')
content1 = '2019-6-21 16:00'
content2 = '2019-6-20 18:00'
content3 = '2019-6-21 17:33'
pattern = re.compile('\d{2}:\d{2}')
content1 = re.sub(pattern, '', content1)
content2 = re.sub(pattern, '', content2)
content3 = re.sub(pattern, '', content3)
print(content1, content2, content3)

