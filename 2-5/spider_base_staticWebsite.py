# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/19 22:51
# @Author : ZQ
# @File : spider_base_staticWebsite
# @Project : python_spider
# --------    -------    --------
import requests
import re
import logging
from urllib.parse import urljoin
# 保存数据为json文本所用库
import json
from os import makedirs
from os.path import exists
# 实现多进程的库
import multiprocessing

# 定义日志输出级别和输出格式
# asctime 表示当前时间 # levelname 表示输出日志级别 # filename 表示文件名称 # lineno 表示输出文件行号 # message 表示输出信息
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10
# 保存数据的文件夹
RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            return response.text
        logging.error('error invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        # exc_info设置为True即可输出Traceback错误堆栈信息
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s', detail_url)
        # yield类似于return后继续这个循环，迭代返回值
        yield detail_url


def scrape_detail(url):
    return scrape_page(url)


def parse_detail(html):
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)
    published_time_pattern = re.compile('(\d{4}-\d{2}-\d{2}).*?上映')
    drama_pattern = re.compile('剧情简介.*?<p.*?>(.*?)</p>', re.S)
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)
    # strip方法去除开头与结尾的空格
    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else []
    published_time = re.search(published_time_pattern, html).group(1).strip() if re.search(published_time_pattern,
                                                                                           html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    score = re.search(score_pattern, html).group(1).strip() if re.search(score_pattern, html) else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_time': published_time,
        'drama': drama,
        'score': score
    }


def save_data(data):
    name = data.get('name')
    name = re.sub(r"[^a-zA-Z0-9\S]", "", name)
    name = re.sub(r"[\s]", '_', name)
    data_path = f'{RESULTS_DIR}/{name}.json'
    # json的dump方法可以将数据保存为文本格式
    # ensure_ascii=False 保证中文字符在文件中能以正常的中文文本呈现，而不是unicode字符
    # indent=2  设置了JSON数据的结果有两行缩进，更美观
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s', data)
        logging.info('saving data to json file')
        save_data(data)
        logging.info('data saved successfully!')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE + 1)
    # 调用map方法，第一个参数为需要被调用的参数main方法，第二个参数就是需要遍历的页码传入main方法的page
    pool.map(main, pages)
    pool.close()
    pool.join()
