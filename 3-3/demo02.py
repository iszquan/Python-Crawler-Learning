# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/23 23:39
# @Author : ZQ
# @File : demo02
# @Project : python_spider
# --------    -------    --------
html = '''
<div id="container">
    <ul class="list">
        <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html">third item</a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
from pyquery import PyQuery as pq

"""
查找节点
"""
''' 
子节点
find方法：所有子孙节点内查找
children：直接子节点内查找
参数内传入CSS选择器 
'''
doc = pq(html)
print(doc.find('li:first-child'))
# print(doc.children('.list'))
'''
父节点
parent：直接父节点
parents：祖先节点(可传入CSS选择器)
'''
# doc = pq(html)
# items = doc('.list')
# print(items.parent())
# print(items.parents())
# print(items.parents('#container'))
'''
兄弟节点
siblings：所有兄弟节点(可传入CSS选择器)
'''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li.siblings())
# print(li.siblings('.item-0'))

"""
遍历节点：返回PyQuery类型
"""
# doc = pq(html)
# lis = doc('li')
# for li in lis.items():
#     print(li, type(li))

"""
获取属性：attr方法
只返回第一个，需要获取多个要采用遍历方法
"""
# doc = pq(html)
# a = doc('a')
# # 下面两个调用方法结果一样
# print(a.attr('href'))
# print(a.attr.href)
# # 遍历
# for item in a.items():
#     print(item.attr('href'))

"""
获取文本
text方法：所有节点内纯文本，组成一个以空格分割的字符串
html方法：节点内HTML文本(带内部节点的文本)，只返回第一个，多个要遍历
"""
# doc = pq(html)
# lis = doc('li')
# print(lis.html())
# print(lis.text())
# for li in lis.items():
#     print(li.html())
