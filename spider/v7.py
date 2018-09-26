'''
使用代理
'''

from urllib import request,error

if __name__ == '__main__':
	url = "http://www.baidu.com"

	#使用代理步骤
	#1设置代理地址
	proxy = {'http':'218.28.191.6:33864'}

	#2创建proxyhandler
	proxy_handler = request.ProxyHandler(proxy)
	#3创建opener
	opener = request.build_opener(proxy_handler)
	#4安装opener
	request.install_opener(opener)

	try:
		rsp = request.urlopen(url)
		html = rsp.read().decode()
		print(html)
	except error.URLError as e:
		print(e)
	except Exception as e:
		print(e)