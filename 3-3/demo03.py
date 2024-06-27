# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/24 16:49
# @Author : ZQ
# @File : demo03
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
节点操作：对节点信息进行动态修改
"""
''' addClass和removeClass '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)
''' attr、text和html '''
''' 只传入一个参数为获取属性，传入两个参数为修改属性 '''
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.text('changed text')
# print(li)
# # text和html修改完成的效果一样 节点内全部被改成传入值
# li.html('111')
# print(li)
''' remove：移除 '''
# doc = pq(html)
# li = doc('li')
# li.remove()
# print(doc)
# # 上下等同
# doc.find('li').remove()
# print(doc)
''' 还有许多操作节点方法,append、empty、prepend等 '''

