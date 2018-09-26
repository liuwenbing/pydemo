
from  urllib import request,parse
##使用parse模块进行参数编码
if __name__=='__main__':

	url = 'http://www.baidu.com/s?'
	wd = input("Input your kwd:")
	qs = {
		"wd":wd
	}
	qs = parse.urlencode(qs)
	print(qs)

	fullurl = url+qs
	print(fullurl)

	rsp = request.urlopen(fullurl)

	html =  rsp.read()
	#如果把bytes内容转化为
	html = html.decode()
	#print(html)


