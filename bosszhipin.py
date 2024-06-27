# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/25 0:38
# @Author : ZQ
# @File : bosszhipin
# @Project : python_spider
# --------    -------    --------
# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/24 22:47
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
from pyquery import PyQuery as pq
from selenium import webdriver
from time import sleep
import multiprocessing

BASE_url = 'https://www.zhipin.com/web/geek/job?query=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&city=101200600'
TOTAL_PAGE = 6


def scrape_url(page):
    url_join = f'&page={page}'
    url = BASE_url + url_join
    yield url


def parse_html(url):
    driver = webdriver.Edge()
    driver.get(url)
    sleep(8)
    html = driver.page_source
    doc = pq(html)
    items = doc('.job-card-wrapper').items()

    with (open('zhipin.txt', 'w', encoding='utf-8') as file):
        for i, item in enumerate(items):
            file.write(f'{i}  ')
            # jobName
            jobName = item.find('.job-name').text()
            file.write(f'工作名称：{jobName}\n')
            # 城市
            city = item.find('.job-area').text()
            file.write(f'城市：{city}\n')
            # 工资
            salary = item.find('.salary').text()
            file.write(f'工资：{salary}\n')
            # 要求
            request = item.find('.tag-list li').text()
            file.write(f'要求：{request}\n')
            # 分割符
            file.write(f'{"=" * 50}\n')
    print('scrape successfully!')


def main(page):
    urls = scrape_url(page)
    for url in urls:
        parse_html(url)


if __name__ == '__main__':
    # pool = multiprocessing.Pool()
    # pages = range(1, TOTAL_PAGE + 1)
    # pool.map(main, pages)
    # pool.close()
    # pool.join()
    for i in range(1, TOTAL_PAGE+1):
        main(i)
