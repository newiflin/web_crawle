from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()            # 声明浏览器Chrome对象
browser.get('https://www.baidu.com')    # 访问页面
print(browser.page_source)

browser.get('https://www.taobao.com')
# 获取单个节点
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
input_fourth = browser.find_element(By.ID, 'q')     # WebElement对象
print(input_first)
print(input_second)
print(input_third)
print(input_fourth)
# 获取多个节点
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)  #   WebElement 列表类型
lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
print(lis)
# 节点交互
input_first.send_keys('iPhone')
time.sleep(1)
input_first.clear()
input_first.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()
# 动作链
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
# 执行javascript  -- 下拉滚动条
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')

