from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get('https://www.inflearn.com/')

delay = 3
driver.implicitly_wait(delay)

driver.find_element_by_xpath('//*[@id="signin"]').click()

driver.find_element_by_xpath('//*[@id="root"]/div[4]/section/form/label[1]/input').send_keys('cowogjs@daum.net')
driver.find_element_by_xpath('//*[@id="root"]/div[4]/section/form/label[2]/input').send_keys('ecsc@qh0ks')

driver.find_element_by_xpath('//*[@id="root"]/div[4]/section/form/button').click()

# ------------- 로그인 완료

