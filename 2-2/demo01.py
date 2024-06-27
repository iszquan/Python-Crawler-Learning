# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/13 16:50
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
import requests

response = requests.get('https://www.baidu.com')
print(type(response))
print(response.status_code)
print(response.headers)
print(response.cookies)
print(type(response.text))
print(response.text[:100])

"""
响应信息
"""
# r = requests.get('https://static1.scrape.center/')
# print(type(r.status_code), r.status_code)   # 状态码
# print(type(r.headers), r.headers)           # 响应头
# print(type(r.cookies), r.cookies)           # Cookie
# print(type(r.url), r.url)                   # URL
# print(type(r.history), r.history)           # 请求历史
#
# # 状态码为200就正常运行
# # requests库内置状态码requests.codes
# # 200为ok，404为not_found
# r = requests.get('https://ssr1.scrape.center/')
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

"""
GET请求
"""
# response = requests.get('https://www.httpbin.org/get')
# print(response.text)

# data = {
#     'name': 'zq',
#     'age': '20'
# }
# response = requests.get('https://www.httpbin.org/get', params=data)
# print(response.text)
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
# }
# r = requests.get('https://www.httpbin.org/get', headers=headers)
# print(r.text)
#
# print(type(response.text))
# # json方法转换JSON格式字符串为字典
# print(type(response.json()))

"""
抓取图片、音频、视频等二进制数据
"""
# response = requests.get('https://scrape.center/favicon.ico')
# # 抓取的图片写入favicon.ico
# with open('favicon.ico', 'wb') as f:
#     f.write(response.content)

"""
POST请求
"""
# data = {
#     'name': 'zq',
#     'age': '20'
# }
# r = requests.post('https://www.httpbin.org/post', data=data)
# print(r.text)
