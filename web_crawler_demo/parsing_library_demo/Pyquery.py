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


