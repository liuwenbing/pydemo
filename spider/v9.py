from urllib import request,parse
from http import cookiejar

cookie = cookiejar.CookieJar()

#生成cookie的管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handle = request.HTTPHandler()

#生成https管理器
https_handle = request.HTTPSHandler()


opener = request.build_opener(http_handle,https_handle,cookie_handle)

def login():
	#刺URL需要提取
	url = "http://www.renren.com/PLogin.do"
	data = {
		"email" :'13119144223',
		"password":"123456"
	}

	data = parse.urlencode(data)

	#创建一个请求对象
	req = request.Request(url,data=data.encode("UTF-8"))
	#使用opener发起请求
	rsp = opener.open(req)

# def getHomePage():
# 	url = "http://www.renren.com/965187997/profile"
# 	#如果已经执行来login函数，
# 	rsp = opener.open(url)
#
# 	html = rsp.read().decode("utf-8")
# 	with open(r'rsp.html', 'w',encoding='utf8') as f:
# 		f.write(html)


if __name__ == '__main__':
	login()

	print(cookie)
	for i in cookie:
		print(i)
		for item in dir(i):
			print(item)
	#getHomePage()



