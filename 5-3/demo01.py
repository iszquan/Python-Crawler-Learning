# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/27 17:01
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
import requests
import logging
import json
from os import makedirs
from os.path import exists
import pymongo

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
LIMIT = 10
TOTAL_PAGE = 10
# RESULTS_DIR = 'results'
# exists(RESULTS_DIR) or makedirs(RESULTS_DIR)
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'spa1'
MONGO_COLLECTION_NAME = 'movies'
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collections = db[MONGO_COLLECTION_NAME]


def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))
    return scrape_api(url)


def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)


# # json方式保存数据
# def save_data(data):
#     name = data.get('name')
#     data_path = f'{RESULTS_DIR}/{name}.json'
#     json.dump(data, open(data_path, 'w', encoding='utf-8'),
#               ensure_ascii=False, indent=2)


# mongodb保存数据
def save_data(data):
    collections.update_one({
        'name': data.get('name')
    }, {
        '$set': data
    }, upsert=True)     # upsert设置为True可以实现存在即更新，不存在即插入的功能


def main():
    for page in range(1, TOTAL_PAGE+1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('detail data %s', detail_data)
            save_data(detail_data)
            logging.info('data saved successfully!')


if __name__ == '__main__':
    main()
