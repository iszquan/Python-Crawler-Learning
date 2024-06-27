# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/15 23:20
# @Author : ZQ
# @File : demo02
# @Project : python_spider
# @FileSummarize ： pyppeteer常用设置
# --------    -------    --------
import asyncio
from pyppeteer import launch

"""
无头模式: headless
"""
# async def main():
#     await launch(headless=False)    # 一般调试时设置为False不开启，生产环境中设置为True开启
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

"""
调试模式: devtools
禁用提示条：args=['--disable-infobars']
防止检测：evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
"""
# async def main():
#     browser = await launch(devtools=True, args=['--disable-infobars'])
#     page = await browser.newPage()
#     await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
#     await page.goto('https://antispider1.scrape.center/')
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

"""
页面大小设置
"""
# width, height = 1366, 768
# async def main():
#     browser = await launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}'])  # 设置窗口大小
#     page = await browser.newPage()
#     await page.setViewport({'width': width, 'height': height})  # 设置显示区域大小
#     await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
#     await page.goto('https://antispider1.scrape.center/')
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

"""
用户数据持久化：会创建一个userdata文件夹存储一些信息
"""
# async def main():
#     browser = await launch(headless=False, userDataDir='./userdata', args=['--disable-infobars'])
#     page = await browser.newPage()
#     await page.goto('https://www.taobao.com')
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

"""
开启无痕模式
"""
width, height = 1366, 768
async def main():
    browser = await launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}'])
    context = await browser.createIncognitoBrowserContext()
    page = await context.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())
