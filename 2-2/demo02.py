# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2023/11/16 20:56
# @Author : ZQ
# @File : demo02
# @Project : python_spider
# --------    -------    --------
###
# requests高级用法
###
import requests

"""
文件上传
"""
# file = {'files': open('favicon.ico', 'rb')}
# r = requests.post('https://www.httpbin.org/post', files=file)
# print(r.text)

"""
Cookie设置
"""
# headers = {'Cookie': 'user_locale=zh-CN; oschina_new_user=false; remote_way=http; slide_id=10; Serve_State=true; yp_riddler_id=ae476530-5b59-471c-9713-c557266b5dae; Hm_lvt_dbba4dc235af9a121ecb9ae949529239=1699010726; BEC=1f1759df3ccd099821dcf0da6feb0357; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22https%3A%2F%2Fgitee.com%2F%3Fchannel_utm_content%3DGitee%2520%257C%2520DevOps%2520%25E7%25A0%2594%25E5%258F%2591%25E6%2595%2588%25E8%2583%25BD%25E5%25B9%25B3%25E5%258F%25B0%26channel_utm_medium%3Dsem%26channel_link_type%3Dweb%26channel_utm_source%3D%25E7%2599%25BE%25E5%25BA%25A6%26sat_cf%3D2%26channel_utm_campaign%3D%25E5%2593%2581%25E4%25B8%2593%26channel_utm_term%3D%25E4%25B8%25BB%25E6%25A0%2587%25E9%25A2%25981%26_channel_track_key%3DWagVxbYD%26link_version%3D1%26wl_src%3Dbaidu%22%7D%7D; Hm_lvt_24f17767262929947cc3631f99bfd274=1698217817,1698983478,1699010726,1700140007; user_return_to_0=%2F%3Fchannel_utm_content%3DGitee%2520%257C%2520DevOps%2520%25E7%25A0%2594%25E5%258F%2591%25E6%2595%2588%25E8%2583%25BD%25E5%25B9%25B3%25E5%258F%25B0%26channel_utm_medium%3Dsem%26channel_link_type%3Dweb%26channel_utm_source%3D%25E7%2599%25BE%25E5%25BA%25A6%26sat_cf%3D2%26channel_utm_campaign%3D%25E5%2593%2581%25E4%25B8%2593%26channel_utm_term%3D%25E4%25B8%25BB%25E6%25A0%2587%25E9%25A2%25981%26_channel_track_key%3DWagVxbYD%26link_version%3D1%26wl_src%3Dbaidu; tz=Asia%2FShanghai; Hm_lpvt_24f17767262929947cc3631f99bfd274=1700140015; gitee_user=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2213442796%22%2C%22first_id%22%3A%2218b94ee4855464-00ea11d6d7e597a-745d5777-2073600-18b94ee48567f7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22gitee%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22sem%22%2C%22%24latest_utm_campaign%22%3A%22enterprise%22%2C%22%24latest_utm_content%22%3A%22competition%22%2C%22%24latest_utm_term%22%3A%22git%22%7D%2C%22%24device_id%22%3A%221889f78a27c5ab-0a2060a41093358-7e56547b-1327104-1889f78a27d10bf%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThhOGQ1Y2I4ZTY4MWQtMDIyMGUyZmU2Mjc3ODk4LTdmNWQ1NDdlLTEzMjcxMDQtMThhOGQ1Y2I4ZTc5NjciLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMzQ0Mjc5NiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2213442796%22%7D%7D; csrf_token=TvUUMFlGER2jRKwYrWCTtD1piMxEYurqxaCWcQZ%2FDJ%2F%2FGRanvdtMLU8CP61mw3jwUdXSAJoU7Xbu4wraztVHpA%3D%3D; gitee-session-n=cXIxOXVES2VZdlphQnlndzhtNUR6eFlhcy9taW1aR0NnRHNqcjJsZGg1MnUrSEZJSmRXMHZXWk5hTk1nKzUyb2VMSWdlcGVBRVRJeWVtYnhZeGNWUUZ0NzV0SUxOWjJqNGpDYjVaRmlRT2tjeUl4c29McHd6TjZybVJxV3RERE5JdmZHbXJuZXdSS2lPV0YyeEpxTE4wOEpxelJWRTlTdmNCZDFxd0FQYzE1SzN1Y09xMGRuVWRXQ28vL0Q3dVU1NnlqajhJMkVtMldWSGtZNytLQ0xEV1FFMUxMV0t4MDNRL3RTb3R6TTJ0d3FkQU5XZzhQZmFHTEhScy8wb2RWRjR3aWVqNE96dFJ5ejVMMkd1T1J3ZndKQTV0ZUJWMmdDN2hGaHN6MmJLOG1uTHV5dUozQ0UyaUpuSlZuMTdqRUE1RnpvYkY4UGlJV3NPVGdhWlR5NGtzd1VPa2tvNThHNXU0VWYyTEVMVndvZEU4RW1tQnFBeDB1Z3dPMUh0RWl4bDJqbEhGVk9Dek9TbWF6dzlIK0Y4Y0FkVUlVZm5lWmk3SFA0eDZHUEphTXFaRlRicy9ZTFNFZTdNZDFZM0xta1o1Y0tobXlHVml4Z2RLT1JxWUNxSkVuYlA0WHRldkwzbkV0RFc0NktIUWc2cERJRXgyYjZrbmhtYVdLR1N3VVpOcGdKZWFwT1RyMitnQ3JDNnFhQ1BDeGFGeDgyUC9OU25MZ21UQm4rdkRFTmgyOGEwQjVNcXNKSUN6VzRHd2QxalBXUGV2bkdKSVNvbFRvU3pZOUJ1TnIwcDIwbkhGYVErQmZCTmpuMDVJaGVCTXMwTWJNNFEwVlJXblBoUElGZS0tMllodFhmamxzT0NYR0RVVWpuelNOUT09--2eb29ec8b042779645cfe49de7e935d6a1a236ac',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
# r = requests.get('https://gitee.com/', headers=headers)
# print(r.text)

"""
Session维持
"""
# # 创建的Session对象s自动帮助维护session的信息
# s = requests.Session()
# s.get('https://httpbin.org/cookies/set/number/123456789')
# r = s.get('https://httpbin.org/cookies')
# print(r.text)

"""
SSL证书验证
"""
# # 通过设置verify参数忽略证书验证
# response = requests.get('https://ssr2.scrape.center/', verify=False)
# print(response.status_code)  # 仍会有警告建议指定证书
# # 忽略警告
# from requests.packages import urllib3
# urllib3.disable_warnings()
# response = requests.get('https://ssr2.scrape.center/', verify=False)
# print(response.status_code)

"""
超时设置
"""
# # 方法一：设置连接和读取的timeout总和
# response = requests.get('https://httpbin.org/get', timeout=1)
# print(response.status_code)
# # 方法二：分别设置连接和读取的timeout
# response = requests.get('https://httpbin.org/get', timeout=(1, 1))
# print(response.status_code)

"""
身份认证
"""
# # 方法一：requests库的自带身份认证功能
# response = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
# print(response.status_code)
# 方法二：OAuth认证
# 需要先安装OAuth库(pip3 install requests_oauthlib)
# from requests_oauthlib import OAuth1
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth)

"""
代理设置:基本HTTP代理
"""
# proxies = {'http': 'http://192.168.10.1',
#            'https': 'http://192.168.10.1'}
# requests.get('https://www.httpbin.org/get', proxies=proxies)

"""
代理设置：socks协议的代理
"""
# # 需要先安装socks库
# proxies = {'http': 'socks5://user:password@host:port',
#            'https': 'socks5://user:password@host:port'}
# requests.get('https://www.httpbin.org/get', proxies=proxies)

"""
Prepared Request
request请求的实现过程
"""
from requests import Request,Session
url = 'https://httpbin.org/post'
data = {'name': 'germey'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
