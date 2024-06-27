# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/17 17:41
# @Author : ZQ
# @File : demo03
# @Project : python_spider
# @FileSummarize ： Playwright常用操作方法
# --------    -------    --------
from playwright.sync_api import sync_playwright
import re
import asyncio
import time

"""
事件监听：on方法
"""
# def on_response(response):
#     if '/api/movie' in response.url and response.status == 200:
#         print(response.json())
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.on('response', on_response)    # 开启事件监听并绑定回调方法on_response
#     page.goto('https://spa6.scrape.center/')    # Ajax加载的网站
#     page.wait_for_load_state('networkidle')
#     browser.close()

"""
获取页面源代码:content()
节点文本：text_content()
"""
# page.content()
# element.text_content()

"""
页面点击:若有多个节点与选择器匹配，只使用第一个
"""
# #            选择器
# page.click(selector)

"""
文本输入(两个必传参数)
"""
# #           选择器     值
# page.fill(selector, value)

"""
获取节点属性(两个必传参数)：只匹配第一个
"""
# #                   选择器    属性名
# page.get_attribute(selector, name)

"""
获取多个节点: 返回ElementHandle对象
"""
# #                        选择器
# page.query_selector_all(selector)
"""
获取单个节点
"""
# page.query_selector(selector)

"""
网络劫持：route(此方法可以实现网络劫持和修改操作)
"""
''' 取消图片加载(不关心图片时，提高爬取效率) '''
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#
#     def cancel_request(route, request):     # 接收两个参数，route代表一个CallableRoute对象，request代表Request对象
#         route.abort()   # 调用CallableRoute对象的abort方法，取消此次请求，导致取消全部图片的加载
#
#     page.route(re.compile(r"(\.png)|(\.jpg)"), cancel_request)  # 对所有包含.png和.jpg的链接请求回调cancel_request方法
#     page.goto('https://spa6.scrape.center/')
#     page.wait_for_load_state('networkidle')
#     page.screenshot(path="no_picture.png")
#     browser.close()
''' 将响应结果修改为自定义文本内容 '''
# 网页显示为custom_response.html
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    def modify_response(route, request):
        route.fulfill(path="./custom_response.html")

    page.route('**/*', modify_response)
    page.goto('https://www.baidu.com')
    time.sleep(10)
    browser.close()
