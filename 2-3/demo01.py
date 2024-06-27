# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/18 20:17
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
import re

"""
match方法：从开头开始匹配
search方法：全局搜索，返回第一个符合条件的
findall方法：全局搜索，返回一个列表，包含所有符合条件的
sub方法：替换匹配到的为指定值
compile方法：将正则表达式转换成一个对象，方便多次使用(可传入re.S等修饰符) 封装正则表达式以方便复用
"""
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}', content)
# print(result)
# # 输出匹配内容
# print(result.group())
# # 输出匹配的范围
# print(result.span())

"""
匹配目标
"""
# content = 'Hello 1234567 World_This is a Regex Demo'
# # ()标记子表达式的开始和结束位置，\d+表示匹配所有数字
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result)
# print(result.group())
# # 输出第一个group内的匹配结果
# print(result.group(1))

"""
通用匹配
用.匹配任意字符，用*重复无数次
^Hello表示以Hello开头，Demo$表示以Demo结尾
?表示非贪婪匹配
"""
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*?Demo$', content)
# print(result)
# print(result.group())

"""
修饰符
re.I 对大小写不敏感
re.L 实现本地化识别匹配
re.M 多行匹配，影响^和$
re.S 使匹配内容包括换行符在内的所有字符
re.U 根据Unicode字符集解析字符。影响\w \W \b \B
re.X 给予你更灵活的格式，以便将正则表达式写的更易于理解
"""
# content = ('''Hello 1234567 World_This
# is a Regex Demo''')
# # re.S使匹配内容包括换行符在内的所有字符
# result = re.match('^Hello.*?(\d+).*?Demo$', content, re.S)
# print(result)  # 输出内包含换行符\n
# print(result.group())
# print(result.group(1))

"""
sub方法
"""
# content = '7sd7s8d7sad7s7f967fs5764fsa'
# result = re.sub('\d+', '', content)
# print(result)

"""
compile方法：封装正则表达式，方便复用
"""
# 可传入re.S等修饰符
pattern = re.compile('\d{2}:\d{2}', re.S)
content = '''2023-11-11 
12:00'''
result = re.sub(pattern, '', content)
print(result)
