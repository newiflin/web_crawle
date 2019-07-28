from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')               #logo节点
print(logo)
# 获取属性
print(logo.get_attribute('class'))
# 获取文本值
input = browser.find_element_by_class_name('zu-top-add-question')   #“提问”按钮节点
print(input.text)
# 获取id
print(input.id)
# 获取位置
print(input.location)
# 获取标签名
print(input.tag_name)
# 获取大小
print(input.size)

# 切换Frame
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('No Logo')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)