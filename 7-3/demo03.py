# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/16 0:05
# @Author : ZQ
# @File : demo03
# @Project : python_spider
# @FileSummarize ： pyppeteer的page操作
# --------    -------    --------
import asyncio
from pyppeteer import launch

"""
选择器：J与querySelector方法等价，JJ与querySelectorAll方法等价
"""
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('https://spa2.scrape.center/')
#     await page.waitForSelector('.item .name')
#     j_result1 = await page.J('.item .name')
#     j_result2 = await page.querySelector('.item .name')
#     j_result3 = await page.JJ('.item .name')
#     j_result4 = await page.querySelectorAll('.item .name')
#     print(j_result1)
#     print(j_result2)
#     print(j_result3)
#     print(j_result4)
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())

"""
选项卡操作: bringToFront()
"""
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://www.baidu.com')
#     page = await browser.newPage()
#     await page.goto('https://www.bing.com')
#     pages = await browser.pages()
#     page = pages[1]
#     await page.bringToFront()
#     await asyncio.sleep(100)
#
# asyncio.get_event_loop().run_until_complete(main())

"""
页面操作
"""
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('https://www.baidu.com')
#     await page.goto('https://spa2.scrape.center/')
#     # 后退
#     await page.goBack()
#     # 前进
#     await page.goForward()
#     # 刷新
#     await page.reload()
#     # 保存pdf
#     await page.pdf(options={'path': 'screenshot.pdf'})
#     # 截图
#     await page.screenshot({'path': 'screenshot.png'})
#     # 设置页面HTML
#     await page.setContent('<h2>Hello World</h2>')
#     # 设置User-Agent
#     await page.setUserAgent('Python')
#     # 设置Headers
#     await page.setExtraHTTPHeaders(headers={})
#     # 关闭
#     await page.close()
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())

"""
点击：click()
"""
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://spa2.scrape.center/')
#     await page.waitForSelector('.item .name')
#     await page.click('.item .name', options={
#         'button': 'right',  # 鼠标按钮，有left、middle、right
#         'clickCount': 1,    # 点击次数，有1和2，代表单击和双击
#         'delay': 3000       # 延迟点击，毫秒
#     })
#     await asyncio.sleep(10)
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())

"""
输入文本：type
"""
# async def main():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://www.taobao.com')
#     await page.type('#q', 'iPad')
#     await asyncio.sleep(10)
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())

"""
获取信息：
"""
# # 源代码
# page.content()
# # Cookies
# page.cookies()

"""
执行JavaScript语句：evaluate
"""
width, height = 1366, 768

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    await asyncio.sleep(2)
    await page.screenshot(path='example.png')
    dimesions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')
    print(dimesions)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

"""
延时等待：WaitForSelector:上述例子用的，等符合条件的节点
waitForFunction：等待某个JavaScript执行完
waitForNavigation：等页面跳转
waitForRequest：等某个特定请求发出
waitForResponse：等某个特定请求对应的响应
waitFor：通用等待方法
waitForXPath：等待符合XPath的节点加载出来
"""