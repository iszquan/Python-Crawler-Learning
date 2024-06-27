# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/9 20:42
# @Author : ZQ
# @File : 2-1
# @Project : python_spider
# --------    -------    --------
"""
爬取页面整体样式
对网页的GET
"""
# import urllib.request
#
# url = 'https://ssr1.scrape.center/'
# response = urllib.request.urlopen(url)
# print(response.read().decode('utf-8'))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

"""
对网页的POST
"""
# from urllib import request, parse
#
# url = 'https://www.httpbin.org/post'
# dict = {'name': 'zq'}
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent', 'Mozills/4.0 (compatible; MSIE 5.5; Windows NT)')
#
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

"""
对URL的识别和分段
"""
from urllib.parse import urlparse, urlunparse, quote, unquote, parse_qs
import requests

# result = urlparse('https://www.baidu.com/index.html;user?id=6#comment')
# print(result)
#
query = urlparse('https://www.httpbin.org/get?name=zq')
data = parse_qs(query.query)
response = requests.post('https://www.httpbin.org/post', data=data)
print(response.text)
#
# data = ['https', 'www.baidu.com', 'index.html', 'user', 'id=5', 'comment']
# print(urlunparse(data))

# keyword = '壁纸'
# url = 'https://www.baidu.com/search?wd='
# print(url + quote(keyword))
#
# unUrl = 'https://www.baidu.com/search?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(unUrl))

"""
robots协议解析
"""
# from urllib.robotparser import RobotFileParser
#
# rp = RobotFileParser()
# rp.set_url('https://www.zhipin.com/robots.txt')
# rp.read()
# print(rp.can_fetch('BaiduSpider', 'https://www.zhipin.com/web/geek/job?query=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&city=101200600'))