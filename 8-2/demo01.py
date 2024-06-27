# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/23 20:40
# @Author : ZQ
# @File : demo01
# @Project : python_spider
# @FileSummarize ： 识别缺口位置
# --------    -------    --------
"""
具体步骤：
(1)对验证码图片进行高斯模糊滤波处理，消除部分噪声干扰
(2)利用边缘检测算法，识别出滑块边缘
(3)基于上步得到的边缘轮廓信息，对比特征，筛选出最可能的轮廓，得到缺口位置
"""
import cv2

GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 450


def get_gaussian_blur_image(image):
    """ 返回高斯滤波处理后的图片信息 """
    #                               高斯滤波处理用的高斯内核大小   高斯内核函数在X方向的标准偏差
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_SIGMA_X)


def get_canny_image(image):
    """ 返回边缘检测后的图片信息 """
    #                          最小判定临界点      最大判定临界点
    return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)


def get_contours(image):
    """ 返回提取的轮廓信息 """
    #                                       轮廓检索模式          轮廓的近似方法
    contours, _ = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def get_contour_area_threshold(image_width, image_height):
    """ 定义目标轮廓的面积上下限 """
    contour_area_min = (image_width * 0.15) * (image_height * 0.25) * 0.8
    contour_area_max = (image_width * 0.15) * (image_height * 0.25) * 1.2
    return contour_area_min, contour_area_max


def get_arc_length_threshold(image_width, image_height):
    """ 定义目标轮廓周长上下限 """
    arc_length_min = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 0.8
    arc_length_max = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 1.2
    return arc_length_min, arc_length_max


def get_offset_threshold(image_width):
    """ 定义缺口位置的偏移量上下限 """
    offset_min = 0.2 * image_width
    offset_max = 0.85 * image_width
    return offset_min, offset_max


# 读取原始图片
image_raw = cv2.imread('captcha.png')
image_height, image_width, _ = image_raw.shape
# 高斯滤波处理
image_gaussian_blur = get_gaussian_blur_image(image_raw)
# 边缘检测处理
image_canny = get_canny_image(image_gaussian_blur)
# 轮廓信息
contours = get_contours(image_canny)
# 遍历各个轮廓信息，筛选目标轮廓信息
contour_area_min, contour_area_max = get_contour_area_threshold(image_width, image_height)
arc_length_min, arc_length_max = get_arc_length_threshold(image_width, image_height)
offset_min, offset_max = get_offset_threshold(image_width)
offset = None
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)  # 计算外接矩形
    if (contour_area_min < cv2.contourArea(contour) < contour_area_max and
            arc_length_min < cv2.arcLength(contour, True) < arc_length_max and
            offset_min < x < offset_max):
        # 标注目标缺口
        cv2.rectangle(image_raw, (x, y), (x+w, y+h), (0, 0, 255), 2)
        offset = x
cv2.imwrite('image_label.png', image_raw)
print('offset: ', offset)
