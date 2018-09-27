'''
破解有道

salt    i = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
 sign = n.md5("fanyideskweb" + e + t + "6x(ZHw]mwzX#u0V7@yfwK")
 t =
 第一  第四个是固定参数,第三个是salt
 第二个参数就是要查找的单词
'''
from urllib import request ,parse

import time,random
import hashlib


def getSalt():
	salt = int(time.time()*1000) +random.randint(0,10)

	return salt


def getMd5(v):
	md5 = hashlib.md5()
	md5.update(v.encode('utf-8'))
	sign = md5.hexdigest()

	return sign


def getSign(key,salt):
	sign = "fanyideskweb" + key + str(salt) + "6x(ZHw]mwzX#u0V7@yfwK"
	sign = getMd5(sign)
	return sign

def youdao(key):
	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
	salt = getSalt()
	data={
		"i": key,
		"from": "AUTO",
		"to": "AUTO",
		"smartresult": "dict",
		"client": "fanyideskweb",
		"salt": str(salt),
		"sign": getSign(key,salt),
		"doctype": "json",
		"version": "2.1",
		"keyfrom": "fanyi.web",
		"action": "FY_BY_REALTIME",
		"typoResult": "false"
	}

	data = parse.urlencode(data).encode('utf-8')

	headers = {
        "Accept":"application/json, text/javascript, */*; q=0.01",
		# "Accept-Encoding": "gzip,deflate",
		"Accept-Language": "zh-CN,zh;q = 0.9",
		"Connection":"keep-alive",
		"Content-Length": "200",
		"Content-Type":"application/x-www-form-urlencoded;charset = UTF-8",
		"Cookie":"DICT_UGC = be3af0da19b5c5e6aa4e17bd8d90b28a |;OUTFOX_SEARCH_USER_ID = 1221241373@59.111.179.141;JSESSIONID = abc7ZIoGtuYka7SXDTAyw;OUTFOX_SEARCH_USER_ID_NCOO = 310819033.95161283;___rl__test__cookies = 1538046437445",
		"Host":"fanyi.youdao.com",
		"Origin":"http://fanyi.youdao.com",
		"Referer":"http://fanyi.youdao.com/User-Agent:Mozilla/5.0(Macintosh;IntelMacOS X 10_13_5) AppleWebKit/537.36(KHTML, likeGecko) Chrome/69.0.3497.100Safari/537.36",
		"X-Requested-With":"XMLHttpRequest"
	}

	req= request.Request(url=url,data=data,headers=headers)

	rsp  = request.urlopen(req)
	html = rsp.read().decode('utf-8')

	print(html)


if  __name__ =='__main__':
	youdao("girl")
