# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/23 15:09
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# @FileSummarize ： CSS位置偏移反爬爬取
# --------    -------    --------
"""
网页通过CSS设置position为absolute绝对定位
再设置left值为多少px控制偏移值来对数据爬取造成干扰
"""
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import re


def parse_name(name_html):
    has_whole = name_html('.whole')
    # 对某些标题未进行CSS偏移的直接进行爬取
    if has_whole:
        return name_html.text()
    # 对有CSS偏移的进行爬取
    else:
        chars = name_html('.char')
        items = []
        for char in chars.items():
            items.append({
                'text': char.text().strip(),
                'left': int(re.search('(\d+)px', char.attr('style')).group(1))
            })
        # 按偏移数值从小到大排序
        items = sorted(items, key=lambda x: x['left'], reverse=False)
        return ''.join([item.get('text') for item in items])


option = ChromeOptions()
option.add_argument('--headless')
browser = webdriver.Chrome(options=option)
browser.get('https://antispider3.scrape.center/')
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.item')))
html = browser.page_source
doc = pq(html)
names = doc('.item .name')
for name_html in names.items():
    name = parse_name(name_html)
    print(name)
browser.close()
