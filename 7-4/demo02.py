# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/17 17:26
# @Author : ZQ
# @File : demo02
# @Project : python_spider
# @FileSummarize ： Playwright选择器用法
# --------    -------    --------
"""
文本选择
"""
# 点击文本内容是Log in的节点
page.click("text=Log in")

"""
CSS选择器
"""
# 根据id或class
page.click(button)
page.click("#nav-bar .contact-us-item")
# 根据特定节点属性
page.click("[data-test=login-button]")
page.click("[aria-label='Sign in']")

"""
CSS选择器+文本值
"""
# 节点内包含指定字符串
page.click("article:has-text('Playwright')")
# 节点中文本与指定字符串完全匹配
page.click("#nav-bar :text('Contact us')")

"""
CSS选择器+节点关系
"""
# has指定另一个选择器
page.click(".item-description:has(.item-promo-banner)")  # 包含.item-promo-banner的.item-description
# 结合相对位置关系
page.click("input:right-of(:text('Username'))")     # 位于文本值为Username的节点右侧的input节点

"""
XPath
"""
page.click("xpath=//button")