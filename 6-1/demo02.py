# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/11 22:34
# @Author : ZQ
# @File : demo02
# @Project : python_spider
# --------    -------    --------
"""
绑定回调: add_done_callback
"""
import asyncio
import requests


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


def callback(task):
    print('Task:', task.result())


coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)    # 绑定回调，task执行完后调用callback方法
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
