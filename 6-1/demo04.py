# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/11 23:25
# @Author : ZQ
# @File : demo04
# @Project : python_spider
# --------    -------    --------
"""
协程实现(非异步请求)： await
"""
'''
协程执行时遇到await事件循环就会将本协程挂起，转而执行其他协程，直至其他协程被挂起或执行完
await后的对象只能是以下3个格式之一：
（1）一个原生协程对象
（2）一个由types.coroutine修饰的生成器，这个生成器可以返回协程对象
（3）由一个包含__wait__方法的对象返回的一个迭代器
'''
import asyncio
import requests
import time

start = time.time()


async def get(url):
    return requests.get(url)


async def request():
    url = 'https://www.httpbin.org/delay/5'
    status = await get(url)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost Time:', end-start)  # 66s，协程还不是异步执行，还需使用异步操作的执行请求
