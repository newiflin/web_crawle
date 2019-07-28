from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 等待延时 —— 隐式等待
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)

# 等待延时 —— 显示等待
browser.get('https://www.taobao.com')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))                   # 等待条件：id为q的搜索框加载出来
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))  # 等待条件：button可点击
print(input, button)
browser.close()

# 浏览器前进和后退
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.python.org')
browser.back()
time.sleep(1)
browser.forward()
browser.close()


