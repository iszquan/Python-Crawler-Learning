# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/16 22:11
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# @FileSummarize ： Playwright几种基本用法
# --------    -------    --------
import asyncio
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright

"""
同步模式: 浏览器上下文管理器调用sync_playwright()方法
"""
# with sync_playwright() as p:    # 定义一个浏览器上下文管理器
#     for browser_type in [p.chromium, p.firefox, p.webkit]:
#         browser = browser_type.launch(headless=False)
#         page = browser.new_page()
#         page.goto('https://www.baidu.com')
#         page.screenshot(path=f'screenshot-{browser_type.name}.png')
#         print(page.title())     # 返回标题(title节点内的文字)
#         browser.close()

"""
异步模式：浏览器上下文管理器调用async_playwright()方法
"""
# async def main():
#     async with async_playwright() as p:
#         for browser_type in [p.chromium, p.firefox, p.webkit]:
#             browser = await browser_type.launch(headless=False)
#             page = await browser.new_page()
#             await page.goto('https://www.baidu.com')
#             await page.screenshot(path=f'screenshot-{browser_type.name}.png')
#             print(await page.title())
#             await browser.close()
#
# asyncio.run(main())

"""
代码生成
例子：              -o输出文件名称  -b指定浏览器
playwright codegen -o script.py -b firefox
"""

"""
支持移动端浏览器
"""
with sync_playwright() as p:
    iphone_14_pro_max = p.devices['iPhone 14 Pro Max']
    browser = p.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_14_pro_max,
        locale='zh-CN'
    )
    page = context.new_page()
    page.goto('https://www.whatismybrowser.com/')
    page.wait_for_load_state(state='networkidle')   # networkidle为网络空闲状态，此处标识页面初始化和数据加载完成状态
    page.screenshot(path='browser-iphone.png')
    browser.close()
