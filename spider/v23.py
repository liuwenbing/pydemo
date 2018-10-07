from urllib import  request

from bs4 import BeautifulSoup
import re

url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content, 'html.parser')
# print(soup.name)
# print("**"*12)
#
#
# for node in soup.head.contents:
# 	if node.name == "meta":
# 		print(node)
# 	if node.name == "title":
# 		print(node.string)
#
# print("**"*12)


# tags = soup.find_all(re.compile("^me"),content='always')
# print(tags)
# print(soup.prettify())

print("**"*12)


titles = soup.select("title")
print(titles[0].string)

