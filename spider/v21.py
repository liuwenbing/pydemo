from urllib import  request

from bs4 import BeautifulSoup


url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content, 'html.parser')


#bs自动转码
content = soup.prettify()
print(content)
