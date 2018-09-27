'''
requests

使用参数headers params
'''
import requests
##两者方式请求
url = "http://www.baidu.com/s?"

#rsp = requests.get(url)

kw = {
	'wd':"王八蛋"
}

headers = {
	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

rsp = requests.get(url,params=kw,headers=headers)
print(rsp.text)

print(rsp.content)

print(rsp.url)

print(rsp.encoding)

print(rsp.status_code)
