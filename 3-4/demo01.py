# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/24 17:41
# @Author : ZQ
# @File : demo01
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
# parsel库需要安装
from parsel import Selector

"""
初始化
"""
# selector = Selector(text=html)
# items = selector.css('.item-0')
# print(len(items), type(items), items)
# items2 = selector.xpath('//li[contains(@class, "item-0")]')
# print(len(items2), type(items2), items2)

"""
提取文本
get方法：提取第一个Selector对象的结果
getall方法：提取所有Selector对象结果，组成列表
"""
# selector = Selector(text=html)
# items = selector.css('.item-0')
# for item in items:
#     text = item.xpath('.//text()').get()
#     print(text)
''' get '''
# selector = Selector(text=html)
# result = selector.xpath('//li[contains(@class, "item-0")]//text()').get()
# print(result)
''' getall '''
# selector = Selector(text=html)
# result = selector.xpath('//li[contains(@class, "item-0")]//text()').getall()
# print(result)
# # css方法版
# result2 = selector.css('.item-0 *::text').getall()
# print(result2)

"""
提取属性
"""
# selector = Selector(text=html)
# # ::attr() css选择器方法
# result = selector.css('.item-0.active a::attr(href)').get()
# print(result)
# # /@ xpath方法
# result2 = selector.xpath('//li[contains(@class, "item-0") and contains(@class, "active")]/a/@href').get()
# print(result2)

"""
正则提取
re对应多个结果
re_first对应第一个符合条件的结果
"""
selector = Selector(text=html)
result = selector.css('.item-0').re('link.*')
print(result)
result2 = selector.css('.item-0').re('link(.*)')
print(result2)
result3 = selector.css('.item-0').re_first('link.*')
print(result3)
