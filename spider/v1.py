#使用urllib来请求网页

from  urllib import request

if __name__=='__main__':
	url = "http://www.xzhizao.com/ask/"
	rsp = request.urlopen(url)


	print("URL: {0}".format(rsp.geturl()))
	print("Info: {0}".format(rsp.info()))
	print("code :{0}".format(rsp.getcode()))

	html =  rsp.read()
	#如果把bytes内容转化为
	html = html.decode()
	#print(html)


