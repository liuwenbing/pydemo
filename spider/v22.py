from urllib import  request

from bs4 import BeautifulSoup


url = 'http://www.baidu.com'

rsp = request.urlopen(url)

content = rsp.read()

soup = BeautifulSoup(content, 'html.parser')


#bs自动转码
content = soup.prettify()


# print(soup.head)
# print("=="*18)
# print(soup.meta)
#
# print("=="*18)

print(soup.link)

print(soup.link.name)

print("=="*18)
print(soup.link.attrs)
print("=="*18)
print(soup.link.attrs['type'])


print("=="*18)




print(soup.title.string)





