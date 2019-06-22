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


