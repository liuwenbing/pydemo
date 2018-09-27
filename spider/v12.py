from  urllib import request
#导入ssl 模块
import  ssl

ssl._create_default_https_context= ssl._create_unverified_context

url = "https://www.12306.cn/mormhwb/"
rsp = request.urlopen(url)

html = rsp.read().decode()

print(html)