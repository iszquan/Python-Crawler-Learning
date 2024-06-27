# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/11 22:02
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
"""
定义协程
"""
import asyncio


# async定义的方法会变成一个无法执行的协程对象，需将此对象注册到事件循环中才能执行
async def execute(x):
    print('Number', x)
    return x

'''
方法一：先创建事件循环loop，再直接利用run_until_complete方法完成注册和启动
'''
# coroutine = execute(1)    # 定义一个协程
# print('Coroutine:', coroutine)  # 方法未被执行，只返回一个协程对象
# print('After calling execute:')
#
# # 创建事件循环
# loop = asyncio.get_event_loop()
# # 将协程对象注册进事件循环并启动
# loop.run_until_complete(coroutine)  # 实质上先将coroutine封装为task对象了
# print('After calling loop')

'''
方法二：不借助loop对象，提前定义好task对象
'''
coroutine = execute(1)
print('Coroutine:', coroutine)  # 方法未被执行，只返回一个协程对象
print('After calling execute:')

task = asyncio.ensure_future(coroutine)
print('Task:', task)    # 此时处于pending状态
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)    # 此时处于finished状态
print('After calling loop')
