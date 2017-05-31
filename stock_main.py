#coding:utf-8
'''
Created on 2017年5月23日 上午8:38:27

@author: caowei13622
'''

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
#import requests
#from requests import Request
#from urllib.parse import urljoin
title = time.strftime('%Y-%m-%d', time.localtime(time.time()))
chromph="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
driver = webdriver.Chrome(chromph)
driver.get('XXXXXX')
fd = open(title+'stock.txt', 'a')
time.sleep(3)
html = driver.page_source
html_tag = BeautifulSoup(html, "html.parser")
#print(html_page.li.string)
#print(html_tag.find_all("div", {"id":"ajax_page1", "class":"new_paging"}))
#print(html_tag.find("div", {"id":"ajax_page1", "class":"new_paging"}).find_all("a"))
#pages = html_tag.find("div", {"id":"ajax_page1", "class":"new_paging"}).find_all("a")
#print(pages[-1])
pgs = html_tag.find("div", {"id":"ajax_page1", "class":"new_paging"}).find_all("a")
pg = pgs[-1]
#print('------',type(pg.get_text()))
dr = re.compile(r'<[^>]+>')
pages = dr.sub('', pg.get_text())
print(pages)
#int(pages)-1
for page in range(int(pages)):
    time.sleep(5)
    html = driver.page_source
    #print(html)
    html_parse = BeautifulSoup(html, "html.parser")
    #print(html_parse.find("div", {"class":"page-main fn-clear"}).get_text())
    """
    保存数据
    """
    fd.write(html_parse.find("div", {"id":"gkcTable","class":"listable"}).get_text())
    fd.write('\r\n')    #换行
    #print(html_parse.find("div", {"id":"gkcTable","class":"listable"}).get_text())
    #driver.find_element_by_link_text(u"下一页").click()
    print(title+'::stock data page:'+str(page))
    if page == int(pages)-1:
        break
    driver.find_element_by_class_name("next").click()

#pageSource2 = driver.page_source
fd.close()
driver.quit()


