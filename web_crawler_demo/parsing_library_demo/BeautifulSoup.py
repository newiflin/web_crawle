from bs4 import BeautifulSoup
import re

print('\n节点选择器')
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.prettify())
print(soup.p.string)    #得到p标签的文本

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were there little sisters; and thei names were
<a href="http://example.com/elseie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottem of a well.</p>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())  #准成标准缩进格式
print(soup.title.string) #title标签的文本

print('\n1.选择元素')
html = '''
<html><head><title>The Dormouse's story</tilte></head>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon atime there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">tacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(type(soup.title)) #Tag类型
print(soup.head)
print(soup.p)

print('\n2.获取信息')
print(soup.title.name) #获取结点名称
print(soup.p.attrs) #获取属性  (字典)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p.string) #获取结点文本

print('\n3.嵌套选择')
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

print('\n4.关联选择')
html = '''
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottem of a well.
</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)  # 获取p结点直接子节点(列表)
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)
print(soup.p.descendants)   #p的子孙结点
for i, child in enumerate(soup.p.descendants):
    print(i, child)

html = '''
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.a.parent)    #获取a节点的直接父节点
print(type(soup.a.parents)) #获取a节点的所有足下节点
print(list(enumerate(soup.a.parents)))

html = '''
<html>
<body>
<p class="story">
            Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
            Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">tillie</a>
            and they lived at the bottom of a well.
</p>
'''
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling', soup.a.next_sibling)
print('Pre Sibling', soup.a.previous_sibling)
print('Next Siblings', list(enumerate(soup.a.next_siblings)))
print('Pre siblings', list(enumerate(soup.a.previous_siblings)))

html='''
<html>
<body>
<p class="story">
            Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie"
class="sister" id="link2">lacie</a>
'''
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])

print('\n5.方法选择器')
html = '''
<div class="panel">
<div class="panel-heading">
<h4>hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name='elements'>
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))
for ul in soup.find_all(name='ul'):
    print(soup.find_all(name='li'))
print()
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in soup.find_all(name='li'):
        print(li.string)

print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='list')) #class是关键字，class_加下划线

html='''
<div class='panel'>
<div class="panel-body">
<a>Hello, this is a link</a>
<a>Hello, this is a link,too</a>
</div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text=re.compile('link')))   #所有匹配正则的文本

#find
print()
html = '''
<div class="panel">
<div class="panel-heading">
<h4>hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name='elements'>
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='element'))

print('CSS选择器')
print(soup.select('ul li'))
print(soup.select('.panel .panel-body'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))
for ul in soup.select('ul'):
    print(ul.select('li'))
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
for li in soup.select('li'):
    print('Get text:', li.get_text())
    print('String:', li.string)