import lxml.html
etree = lxml.html.etree

#解析库lxml    (xpah方式)
print('1.解析')
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-0"><a href="link4.html">fourth item</a></li>
<li class="item-1"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)         #可以修正后的html
result = etree.tostring(html)
print(result.decode('UTF-8'))

print('\n')
html = etree.parse('./test.html', etree.HTMLParser())   #读取文本进行解析
result = etree.tostring(html)
print(result.decode('UTF-8'))

print('\n2.所有结点')
result = html.xpath('//*')
print(result)

print('\n3.子节点')
result = html.xpath('//li/a')
print(result)

print('\n4.父节点')
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

print('\n5.属性匹配')
result = html.xpath('//li[@class="item-0"]')
print(result)

print('\n6.文本获取')
result = html.xpath('//li[@class="item-0"]//text()')    #获取所有子孙结点文本
print(result)
result = html.xpath('//li[@class="item-0"]/a/text()')   #获取子节点a标签的文本
print(result)

print('\n7.属性获取')
result = html.xpath('//li/a/@href')
print(result)

print('\n8.属性多值匹配')
text = '''
<li class="li li-class"><a href="index.html">first-item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

print('\n9.多属性匹配')
text = '''
<li class="li li-class" name="item"><a href="link-html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

print('\n10.按序选择')
html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//li[1]/a/text()')     #选择第一个li结点的直接子节点a的文本
print(result)
result = html.xpath('//li[last()]/a/text()')    #选择倒数第一个...
print(result)
result = html.xpath('//li[position()<3]/a/text()') #选择位置小于3...
print(result)
result = html.xpath('//li[last()-2]/a/text()') #选择倒数第三个...
print(result)

print('\n11.节点轴选择')
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html"><span>second item</span></a></li>
<li class="item-inactive"><a href="link3.html"><span>third item</span></a></li>
<li class="item-0"><a href="link4.html"><span>fourth item</span></a></li>
<li class="item-1"><a href="link5.html"><span>fifth item</span></a>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)
