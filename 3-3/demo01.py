# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/23 23:17
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
html = '''
<div id="container">
    <ul class="list">
        <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
from pyquery import PyQuery as pq
import requests

"""
初始化
"""
''' 字符串初始化 '''  # 最常用方法
# doc = pq(html)
# print(doc('li'))    # 选择所有li节点
''' URL初始化 '''
# doc01 = pq(url='https://www.baidu.com')
# print(doc01('title'))
# # 上下两个方法等同
# doc02 = pq(requests.get('https://www.baidu.com').text)
# print(doc02('title'))
''' 文件初始化 '''
# doc = pq(filename='test.html')
# print(doc('li'))

"""
基本CSS选择器    text()方法获取节点的文本内容
"""
# doc = pq(html)
# # 传入CSS选择器#container .list li
# print(doc('#container .list li'))
''' 遍历获取 '''
# doc = pq(html)
# for item in doc('#container .list li').items():
#     print(item.text())

"""
伪类选择器
"""
# doc = pq(html)
''' 第一个节点 '''
# li = doc('li:first-child')
# print(li)
''' 最后一个节点 '''
# li = doc('li:last-child')
# print(li)
''' 第二个节点 '''
# li = doc('li:nth-child(2)')
# print(li)
''' 偶数位置节点 '''
# li = doc('li:nth-child(2n)')
# print(li)
''' 第三个li节点之后的li节点 '''
# li = doc('li:gt(2)')
# print(li)
''' 包含指定文本的节点 '''
# li = doc('li:contains(fifth)')
# print(li)
