# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/13 23:23
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
"""
基本用法
"""
# 需安装selenium和Chromedrive
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 初始化浏览器对象
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element(By.ID, 'kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
