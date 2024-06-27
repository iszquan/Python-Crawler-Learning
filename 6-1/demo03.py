# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/11 23:04
# @Author : ZQ
# @File : demo03
# @Project : python_spider
# --------    -------    --------
"""
多任务协程: wait
"""
import asyncio
import requests


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

# 创建5个task，组成列表
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Task:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task Result:', task.result())
