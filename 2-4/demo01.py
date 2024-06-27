# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/18 21:31
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
"""
httpx : 用于爬取强制使用HTTP/2.0的网站
urllib和requests都只支持HTTP/1.1
"""
# 需要先安装httpx ，若要支持HTTP/2.0还要安装对2.0的支持模块“httpx[http2]"
import httpx

"""
get、post等请求与requests库基本类似
"""

"""
开启对HTTP/2.0的支持
"""
# # 声明一个Client对象，设置http2参数为True
# client = httpx.Client(http2=True)
# response = client.get('https://spa16.scrape.center')
# print(response.status_code)
# # http_version属性，返回http版本，而requests中不存在该属性
# print(response.http_version)

"""
Client对象
"""
# # Client对象类比requests中的Session持久化对象
# # 官方推荐写法：with as语句
# with httpx.Client(http2=True) as client:
#     response = client.get('https://spa16.scrape.center')
#     print(response)
# # 上述用法等价方法：
# client = httpx.Client(http2=True)
# try:
#     response = client.get('https://spa16.scrape.center')
#     print(response)
# finally:
#     client.close()  # 此类写法需要显式调用close()来关闭client

"""
声明Client对象时传入参数方法
"""
# url = 'https://www.httpbin.org/headers'
# headers = {'User-Agent': 'my-app/0.0.1'}
# with httpx.Client(headers=headers) as client:
#     response = client.get(url)
#     print(response.json()['headers']['User-Agent'])   # http2.0返回信息不限格式，有可能不是json格式的，故有的不能用json()方法

"""
异步请求
"""
# # httpx支持异步客户端请求，支持Python的async请求模式 (暂时了解即可)
# import asyncio
#
#
# async def fetch(url):
#     async with httpx.AsyncClient(http2=True) as client:
#         response = await client.get(url)
#         print(response.text)
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(fetch('https://www.httpbin.org/get'))
