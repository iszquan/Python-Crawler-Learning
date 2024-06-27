# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/20 21:04
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
# lxml库需要先安装
from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''

"""
XPath解析基础
"""
# # 方法一
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))   # tostring后为bytes类型，用decode转换为str类型
# # 方法二: 不声明，直接读取文本文件进行解析
# html = etree.parse('./test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

"""
找子节点: //获取节点的所有子孙节点, /获取节点的直接子节点
"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result01 = html.xpath('//*')  # *代表匹配所有节点
# print(result01)
# result02 = html.xpath('//li')    # 指定获取所有li节点
# print(result02)
# result03 = html.xpath('//li/a')     # 获取所有li节点的所有直接a子节点
# print(result03)
# result04 = html.xpath('//ul//a')    # 获取所有ul的所有a子孙节点
# print(result04[0])
# # 错误示范
# result05 = html.xpath('//ul/a')     # ul节点下无直接的a节点，返回空列表
# print(result05)

"""
找父节点: 用..实现或者parent::实现
"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result01 = html.xpath('//a[@href="link4.html"]/../@class')
# print(result01)
# result02 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result02)

"""
属性匹配： 用@实现属性过滤
[]实现限制属性，下文的无[]的为属性获取
"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]')
# print(result)

"""
文本获取: text方法
"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)   # 自动修正的html导致最后一个li节点中包含\r\n换行符信息

"""
属性获取
"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)

"""
属性多值匹配: contains方法，传入第一个参数为属性名，第二个参数为属性值
"""
# text02 = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text02)
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)

"""
多属性匹配： and、or等运算符
"""
# text03 = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text03)
# result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result)

"""
按序选择：往中括号中传入索引实现获取特定节点
"""
# html = etree.parse('./test.html', etree.HTMLParser())
# result01 = html.xpath('//li[1]/a/text()')
# print(result01)
# result02 = html.xpath('//li[last()]/a/text()')
# print(result02)
# result03 = html.xpath('//li[position()<3]/a/text()')
# print(result03)
# result04 = html.xpath('//li[last()-2]/a/text()')
# print(result04)

"""
节点轴选择
ancestor轴：获取祖先节点
attribute轴：获取属性值
child轴：获取子节点
descendant轴：获取子孙节点
following轴：获取当前节点后的节点
following-sibling轴：获取当前节点后的同级节点
"""
html = etree.parse('./test.html', etree.HTMLParser())
result01 = html.xpath('//li[1]/ancestor::*')    # 获取所有祖先节点
print(result01)
result02 = html.xpath('//li[1]/ancestor::div')  # 获取div这个祖先节点
print(result02)
result03 = html.xpath('//li[1]/attribute::*')   # 获取li[1]的所有属性值
print(result03)
result04 = html.xpath('//li[1]/child::*')       # 获取子节点
print(result04)
result05 = html.xpath('//li[1]/descendant::span')     # 获取子孙节点
print(result05)
result06 = html.xpath('//li[1]/following::*')    # 获取当前节点后所有节点
print(result06)
result07 = html.xpath('//li[1]/following-sibling::*')   # 获取当前节点后所有同级节点
print(result07)
