#! -*- coding:utf-8 -*-


import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException
from selenium import webdriver

def call_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    time.sleep(1)
    return html


# 正则和lxml混用
def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
	patt = re.compile("uid=(.*?)&mid=(.*?)&pid=(.*?)&pic_objects",re.S)
	items = re.findall(patt,html)
	return items



url = 'https://weibo.com/p/1005056060411362/photos?from=page_100505#wbphoto_nav'
html = call_page(url)
c = parse_html(html)
print(html)





