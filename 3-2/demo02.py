# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/22 23:23
# @Author : ZQ
# @File : demo02
# @Project : python_spider
# --------    -------    --------
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

"""
关联选择
"""
from bs4 import BeautifulSoup

'''
contents 子节点：选择节点内包含的所有内容 列表形式返回
'''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.contents)
'''
children 子节点，以生成器类型返回
'''
# # enumerate将其组成一个索引序列，利用它可以同时获得索引和值
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.children)  # 返回生成器类型
# for i, child in enumerate(soup.p.children):
#     print(i, child)
'''
descendants 子孙节点（所有子、孙节点），以生成器类型返回
'''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)

'''
parent 父节点（直接父节点） 返回父节点内容
'''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.a.parent)
'''
parents 祖先节点，以生成器类型返回
'''
# soup = BeautifulSoup(html, 'lxml')
# print(list(enumerate(soup.p.parents)))

'''
同级节点 兄弟节点
'''
# soup = BeautifulSoup(html, 'lxml')
# # next_sibling：下一个兄弟节点
# print(soup.a.next_sibling)
# # previous：上一个兄弟节点
# print(soup.a.previous_sibling)
# # next_siblings：后面所有兄弟节点
# print(list(enumerate(soup.a.next_siblings)))
# # previous_siblings：前面所有兄弟节点
# print(list(enumerate(soup.a.previous_siblings)))
