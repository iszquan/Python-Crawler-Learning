# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/23 0:02
# @Author : ZQ
# @File : demo03
# @Project : python_spider
# --------    -------    --------
html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

from bs4 import BeautifulSoup
import re

"""
方法选择器
find_all(name, attrs , recursive , **kwargs)
以下方法同样适用：
find , find_parent , find_parents , find_next_sibling , find_next_siblings , 
find_previous_sibling , find _previous siblings , find_next , find_all_next , find_all_previous , find_previous
"""
''' name '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(name='ul'))
# print(soup.find_all(name='ul')[0])
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
''' attrs '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))  # class为python关键字，所以要加_
''' text '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text=re.compile('ay')))
# # 上下两句同等
# print(soup.find_all(string=re.compile('ay')))

"""
css选择器：select方法  选择到的节点组成列表返回
"""
# soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(soup.select('ul')[0])
''' 嵌套选择 '''
# soup = BeautifulSoup(html, 'lxml')
# for ul in soup.select('ul'):
#     print(ul.select('li'))
''' 获取属性 '''
#     print(ul['id'])
''' 
获取文本： get_text方法 或 string属性
'''
soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
    print(li.get_text())
    print(li.string)
