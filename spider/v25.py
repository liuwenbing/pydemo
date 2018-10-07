'''
selenium操作百度
'''
from  selenium import  webdriver
import  time
#通过keys模拟键盘
from selenium.webdriver.common.keys import Keys

#操作那个浏览器就对哪个浏览器见一个实例
#自动按照环境变量查找浏览器
driver = webdriver.PhantomJS('/usr/local/phantomjs-2.1.1-macosx/bin/phantomjs')

#如果没有浏览器，需要指定


driver.get("http://www.baidu.com")


#通过函数查找title
print("title:{0}".format(driver.title))