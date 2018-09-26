
'''
利用parse模块模拟post
分析百度字典步骤
检查返回格式，json,需要使用json包
'''
from urllib import request,parse
import json
#负责处理json包格式

baseurl = 'https://fanyi.baidu.com/sug'

#存放用来模拟form的数据dict格式

data = {
	#
	'kw':'girl'
}

# 需要parse 编码  str

data = parse.urlencode(data).encode("utf-8")



##我们需要构造一个请求头，请求头部分至少传入数据的长度
headers = {
	'Content-Length':len(data)
}


#可以尝试

rsp = request.urlopen(baseurl,data=data)

json_dat = rsp.read().decode('utf-8')


json_dat = json.loads(json_dat)
print(type(json_dat))
print(json_dat['data'])

for item in json_dat['data']:
	print(item['v'],'---',item['k'])
