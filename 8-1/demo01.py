# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/23 16:25
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# @FileSummarize ： 
# --------    -------    --------
import tesserocr
from PIL import Image
import numpy as np

image = Image.open('captcha3.png')
# 将图片转化为灰度图片
image = image.convert('L')
threshold = 100  # 灰度阈值
# 将图片转化为numpy数组
array = np.array(image)
array = np.where(array > threshold, 255, 0)     # 将灰度大于阈值的图片像素设置为255,表示白色,否则设置为0,表示黑色
# 将numpy数组转化为图像
image = Image.fromarray(array.astype('uint8'))
print(tesserocr.image_to_text(image))
