# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/11 23:50
# @Author : ZQ
# @File : demo05
# @Project : python_spider
# --------    -------    --------
"""
异步请求与协程的配合使用
"""
# aiohttp库需先安装
import asyncio
import aiohttp
import time

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response


async def request():
    url = 'https://www.httpbin.org/delay/5'
    response = await get(url)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost Time:', end-start)  # 6s
