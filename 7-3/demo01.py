# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/15 22:40
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# @FileSummarize ： 基础使用(快速上手pyppeteer)
# --------    -------    --------
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    # 启动浏览器
    browser = await launch()
    # 新建选项卡
    page = await browser.newPage()
    # 跳转网页
    await page.goto('https://spa2.scrape.center/')
    # 等待加载
    await page.waitForSelector('.item .name')
    # 获取源码
    doc = pq(await page.content())
    names = [item.text() for item in doc('.item .name').items()]
    print('Names:', names)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
