from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Cookies
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'heart'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
browser.close()

# 选项卡管理
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')                 #打开一个新的选项卡
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])     #切换到第二个选项卡
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])     #切换到第一个选项卡
browser.get('https://www.python.org')
browser.close()

# 异常处理
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_class_name('hello')
except NoSuchElementException:
    print('Not Found')
finally:
    browser.close()
