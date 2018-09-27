from urllib import request,parse
from http import cookiejar

filename= "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)

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

	#保存
	##ignore_discard 表示cookie将要被丢弃也要保存下来
	cookie.save(ignore_discard=True, ignore_expires=True)


if __name__ == '__main__':
	login()




