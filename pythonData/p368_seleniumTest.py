#!/usr/bin/env python

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
print(type(driver))
print('-' * 50)

print('go Google~!!')
url = 'http://www.google.com'
driver.get(url)

search_textbox = driver.find_element(By.NAME, 'q')
word = 'selenium'
search_textbox.send_keys(word)

search_textbox.submit()

wait = 3
print(str(wait) + '동안 기다립니다.')
time.sleep(wait)

imagefile = 'xx_capture.png'
driver.save_screenshot(imagefile)
print(imagefile + '저장 완료')

wait = 3
driver.implicitly_wait(wait)

driver.quit()
print('Browser Exit~!!')