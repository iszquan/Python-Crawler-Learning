# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/12/15 15:11
# @Author : ZQ
# @File : demo02
# @Project : python_spider
# --------    -------    --------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import time
"""
访问页面：get
"""
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# print(browser.page_source)
# browser.close()

"""
查找节点
"""
''' 单个节点: find_element '''
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input_first = browser.find_element(By.ID, 'q')
# input_second = browser.find_element(By.CSS_SELECTOR, '#q')
# input_third = browser.find_element(By.XPATH, '//*[@id="q"]')
# print(input_first, input_second, input_third)
# browser.close()
''' 多个节点: find_elements '''
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
# print(lis)
# browser.close()

"""
节点交互(点击等事件)
"""
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# input = browser.find_element(By.ID, 'q')
# input.send_keys('IPhone')   # 输入文字
# time.sleep(1)   # 等待一秒
# input.clear()   # 清空输入框
# input.send_keys('iPad')
# button = browser.find_element(By.CLASS_NAME, 'btn-search')
# button.click()  # 点击搜索键，实现搜索

"""
动作链(鼠标拖曳等动作)
"""
# browser = webdriver.Chrome()
# url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')    # 根据id：iframeResult切换窗口到iframeResult部分
# source = browser.find_element(By.CSS_SELECTOR, '#draggable')    # 拖曳对象
# target = browser.find_element(By.CSS_SELECTOR, '#droppable')     # 拖曳目标地
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)   # 声明拖曳对象和拖曳目标
# actions.perform()

"""
运行JavaScript(下拉进度条等)：execute_script方法
"""
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')    # 拉到页面最底部
# browser.execute_script('alert("To Bottom")')
# time.sleep(2)

"""
获取节点信息
"""
''' 获取属性 '''
# browser = webdriver.Chrome()
# url = 'https://spa2.scrape.center/'
# browser.get(url)
# logo = browser.find_element(By.CLASS_NAME, 'logo-image')
# print(logo)
# print(logo.get_attribute('src'))    # 获取src属性
''' 获取文本 '''
# print(logo.text)
''' 获取ID、位置、标签名、大小 '''
# browser = webdriver.Chrome()
# url = 'https://spa2.scrape.center/'
# browser.get(url)
# input = browser.find_element(By.CLASS_NAME, 'logo-title')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

"""
切换frame: switch_to
selenium打开页面默认操作父frame，不能获取子frame节点，所以需要切换
"""
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')     # 切换到子frame(无logo节点)
# try:
#     logo = browser.find_element(By.CLASS_NAME, 'logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()            # 切换回父frame(有logo节点)
# logo = browser.find_element(By.CLASS_NAME, 'logo')
# print(logo)
# print(logo.text)

"""
延时等待
"""
''' 隐式等待(效果不好)：节点未加载出时，等待规定时间再进行查找 '''
''' 显示等待：规定最长等待时间，该时间内加载出信息则立刻返回信息， 未加载出则抛出异常 '''
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)   # 最长等待10s
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))    # 条件：节点出现
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))   # 条件：按钮可点击
# print(input)
# print(button)

"""
前进：forward
后退：back
"""
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.get('https://www.taobao.com')
# browser.get('https://www.python.org')
# browser.back()
# time.sleep(1)
# browser.forward()
# time.sleep(1)
# browser.close()

"""
Cookie: add_cookie()
"""
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com')
# print(browser.get_cookies())
# # 传入字典
# browser.add_cookie({'name': 'zhengquan', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# # 删除所有cookie
# browser.delete_all_cookies()
# print(browser.get_cookies())

"""
选项卡管理
"""
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# # 新开一个选项卡
# browser.execute_script('window.open()')
# print(browser.window_handles)   # 获取当前开启的所有选项卡
# # 切换到第二个选项卡
# browser.switch_to.window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# # 切换回第一个选项卡
# browser.switch_to.window(browser.window_handles[0])
# time.sleep(1)
# browser.get('https://www.zhihu.com')

"""
异常处理
"""
# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
# except TimeoutException:
#     print('Time Out')
# try:
#     browser.find_element(By.ID, 'hello')
# except NoSuchElementException:
#     print('No Such Element')
# finally:
#     browser.close()

"""
反屏蔽 (原理：window.navigator中是否包含webdriver属性)
"""
# # 大多情况可以用CDP解决，据此可实现在页面刚开始加载时就执行JavaScript语句，将webdriver属性置空
# # CDP：Chrome Devtools Protocol，Chrome开发工具协议
# option = ChromeOptions()
# # 隐藏WebDriver提示条
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# # 自动化扩展信息
# option.add_experimental_option('useAutomationExtension', False)
# browser = webdriver.Chrome(options=option)
# # 执行CDP方法Page.addScriptToEvaluateOnNewDocument，并将JavaScript方法传入使webdriver属性置空
# browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
#     'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
# })
# browser.get('https://antispider1.scrape.center/')

"""
无头模式(不弹出窗口)
"""
# option = ChromeOptions()
# option.add_argument('--headless')   # add_argument方法传入参数--headless即开启无头模式
# browser = webdriver.Chrome(options=option)
# browser.set_window_size(1366, 768)  # 窗口大小设置
# browser.get('https://www.baidu.com')
# browser.get_screenshot_as_file('preview.png')   # 输出页面截图
