# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/24 22:47
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
import requests
from pyquery import PyQuery as pq
import re

url = 'https://ssr1.scrape.center/'
html = requests.get(url).text
doc = pq(html)
items = doc('.el-card').items()

with (open('movies.txt', 'w', encoding='utf-8') as file):
    for item in items:
        # 电影名
        name = item.find('a > h2').text()
        file.write(f'电影名称：{name}\n')
        # 类别
        categories = [item.text() for item in item.find('.categories button span').items()]
        for i, category in enumerate(categories):
            if i+1 == len(categories):
                file.write(f'{category}\n')
            elif i == 0:
                file.write(f'类别：{category}  ')
            else:
                file.write(f'{category}  ')
        # 上映时间
        published_time = item.find('span:contains(上映)').text()
        published_time = re.search('(\d{4}-\d{2}-\d{2})', published_time).group(1) \
            if published_time and re.search('(\d{4}-\d{2}-\d{2})', published_time) else None
        file.write(f'上映时间：{published_time}\n')
        # 评分
        score = item.find('.score').text()
        file.write(f'评分：{score}\n')
        # 分割符
        file.write(f'{"=" * 50}\n')
print('scrape successfully!')
