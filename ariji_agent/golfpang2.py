#-*- coding:utf-8 -*-
# 골팡 agent 찾기
# 임포트
import json
import time
import datetime

# bs4 임포트
from bs4 import BeautifulSoup

# selenium 임포트
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("disable-gpu")

# webdriver 설정(Chrome, Firefox 등) - Headless 모드 / 브라우저가 실행되지 않음
browser = webdriver.Chrome('/Users/tess/Documents/ariji_agent/ariji_agent/webdriver/chromedriver', options=chrome_options)

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# golfpnag 부킹 페이지 이동
browser.get('http://www.golfpang.com/web/round/booking_list.do')
time.sleep(2)

# 한강 이남 골프장 선택
browser.find_element_by_xpath('//*[@id="Msection2"]/div[2]/div/div/ul/li[1]/div[2]/div[2]').click()
time.sleep(1)

# 골프장 검색(아리지 no.61)
browser.find_element_by_xpath('//*[@id="sct2"]/option[77]').click()

# 검색하기
browser.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/table/tbody/tr[5]/td/span/a/span').click()
time.sleep(2)
#print('Page Contents : {}'.format(browser.page_source))

soup = BeautifulSoup(browser.page_source, "html.parser")
#print(soup.prettify())

# 골프장 리스트 선택
golfpang_agent = soup.select('#tblList > div > table')
#print(golfpang_agent)

'''
http://www.golfpang.com/web/round/booking_tblList.do

pageNum: 1
bkOrder: 
rd_date: 2020-05-06
ampm: 
sector: 5
idx: 
cust_nick: 
clubname: 58
'''

# BeautifulSoup 인스턴스 삭제
del soup

# 브라우저 종료
browser.quit()

