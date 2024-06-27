# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/25 15:09
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
import csv
import pandas as pd

"""
写入
"""
''' 单行写入：writerow '''
# # 设置newline就会无多余空行
# with open('data.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')    # writer方法初始化写入对象 delimiter设置列之间的分隔符，默认为逗号
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['1001', 'Mike', 20])
#     writer.writerow(['1002', 'Bob', 18])
#     writer.writerow(['1003', 'Jordan', 22])
''' 多行写入：writerows '''
# with open('data2.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerows([['1001', 'Mike', 20], ['1002', 'Bob', 18], ['1003', 'Jordan', 22]])
''' 字典写入(爬虫大多情况) '''
# with open('data3.csv', 'w', newline='') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     # 初始化字典写入对象
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     # writerheader方法写入头信息
#     writer.writeheader()
#     writer.writerow({'id': '1001', 'name': 'Mike', 'age': 20})
#     writer.writerow({'id': '1002', 'name': 'Bob', 'age': 18})
#     writer.writerow({'id': '1003', 'name': 'Jordan', 'age': 22})
#     writer.writerows([{'id': '1001', 'name': 'Mike', 'age': 20}, {'id': '1002', 'name': 'Bob', 'age': 18}])
''' pandas方法 '''
# data = [
#     {'id': '1001', 'name': 'Mike', 'age': 20},
#     {'id': '1002', 'name': 'Bob', 'age': 18},
#     {'id': '1003', 'name': 'Jordan', 'age': 22}
# ]
# df = pd.DataFrame(data)
# df.to_csv('data4.csv', index=False)

"""
读取
"""
''' 利用csv库 '''
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)
''' pandas '''
# df = pd.read_csv('data.csv')
# print(df)
''' df转为列表 '''
df = pd.read_csv('data.csv')
data = df.values.tolist()
print(data)
# 遍历 iterrows用于对dataframe对象的遍历
for index, row in df.iterrows():
    print(row.tolist())
