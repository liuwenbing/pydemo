'''
ajax爬取

https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=80&limit=20
'''

from urllib import request ,parse
import json

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=80&limit=20"

rsp = request.urlopen(url)

data = rsp.read().decode()

data = json.loads(data)

print(data)