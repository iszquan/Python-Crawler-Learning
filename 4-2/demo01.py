# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/25 14:53
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# --------    -------    --------
"""
loads：将json字符串转化为json对象
load：将整个文件内容转化为json对象
dumps：将json对象转换为json字符串
dump：将json对象全部写入文件
"""
import json

# ensure_ascii=False 保证中文字符在文件中能以正常的中文文本呈现，而不是unicode字符
# indent=2  设置了JSON数据的结果有两行缩进，更美观
