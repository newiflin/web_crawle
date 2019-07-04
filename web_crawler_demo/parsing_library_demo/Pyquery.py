from pyquery import PyQuery as pq

# pyquery解析库
print('1.初始化')
print('1.1 字符串初始化')
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html);
print(doc('li'))

print('1.2URL初始化')
doc = pq('https://cuiqingcai.com')
print(doc('title'))

print('1.3 文件初始化')
doc = pq(filename='demo.html')
print(doc('li'))

print('2.基本CSS选择器')
doc=pq(html)
print(doc('#container .list li'))
print(type(doc('#container .list li')))     #pyquery对象

print('3.查找节点')
print('3.1 查找子节点')
item = doc('.list')
print(item)
print(type(item))
lis = item.find('li')   #find找到item的所有li节点(子孙节点)
print(lis)
print(type(lis))
lis = item.children()  #children查找子节点
print(type(list))
print(lis)
lis = item.children('.active')  #筛选子节点
print(lis)

print('3.2 父节点')
container = item.parent()   #获取父节点
print(container)
print(type(container))      #pyquery对象
containers = item.parents()  #获取祖先节点
print(containers)
print(type(containers))
containers = item.parents('.wrap') #删选祖先节点
print(containers)

print('3.3 兄弟节点')
doc = pq(html)
li = doc('.item-0.active')
print(li.siblings())    #获取兄弟节点
print(li.siblings('.active')) #筛选兄弟节点

print('4.遍历')
li = doc('.item-0.active')
print(li)
print(str(li))
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))

print()
print('5.获取信息')
print('5.1 获取属性')
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)

a = doc('a')
print(a, type(a))
print(a.attr('href'))   #多个节点，只会得到第一个节点的属性
print(a.attr.href)
for item in a.items():
    print(item.attr('href'))
print()
print('5.2 获取文本')
a = doc('.item-0.active a')
print(a)
print(a.text())
li = doc('.item-0.active')
print(li)
print(li.html())

li = doc('li')          #选中多个节点
print(li.html(), type(li.html())) #返回第一个节点的html文本
print(li.text(), type(li.text())) #返回所有文本组成的字符串

print('6.节点操作')
print('addClass removeClass')
li = doc('.item-0.active')
print(li)
li.remove_class('active')
print(li)
li.add_class('active')
print(li)

print('attr text html')
html = '''
<ul>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name', 'tql')
print(li)
li.text('stay hungry')
print(li)
li.html('<span><changed item</span>')
print(li)

print('remove')
html = '''
<div class="wrap">
    Hello, Worldb
<p>This is a paragraph</p>
</div>
'''
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())

print('7.伪类选择器')
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')    #第三个li节点之后的节点（这里就是第4和第5个li节点）
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)