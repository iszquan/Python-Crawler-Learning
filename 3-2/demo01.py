# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/21 0:02
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup

"""
基本使用
"""
# soup = BeautifulSoup(html, 'lxml')  # BeautifulSoup对象初始化
# print(soup.prettify())  # prettify方法，以标准缩进格式输出
# print(soup.title.string)
# print(soup.title.name)
# print(type(soup.title))
# print(soup.p)   # 只会选择第一个匹配到的p节点

"""
提取信息
"""
# soup = BeautifulSoup(html, 'lxml')
# # 获取名称
# print(soup.title.name)
# # 获取属性
# print(soup.p.attrs)
# print(soup.p['name'])  # 选择属性
# # 获取内容
# print(soup.title.string)

"""
嵌套选择
"""
# soup = BeautifulSoup(html, 'lxml')
# print(soup.head.title)
# print(soup.head.title.string)
