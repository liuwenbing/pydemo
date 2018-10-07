''''''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url)


text = driver.find_element_by_id('wrapper').text


print(text)
print(driver.title)

driver.save_screenshot("index.png")
#id= kw 的输入框
driver.find_element_by_id('kw').send_keys(u"大熊猫")


#ID= su  是百度的搜索按钮，click点击

driver.find_element_by_id('su').click()

time.sleep(5)

driver.save_screenshot('daxiaongmao.png')

#得到cookie
print(driver.get_cookies())


#模拟输入两个键  ctrl +a

# driver.find_element_by_id('kw').send_keys(Keys.CONCTOL,'a')
