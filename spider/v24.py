'''
:正则re
步骤  1，compile函数以便一个pattern对象
	 2，通过pattern 对象的一些列方法对文本进行匹配，匹配结果是一个match 对象
	 3，用match 对象的方法，对结果进行操作
'''

import  re
#r表示后面是原字符串
s = r'\d+'

pattern  = re.compile(s)

m = pattern.match("one12two3three3")
print(m)

#match还可以带位置参数
m1 = pattern.match("one12two3three3",3,10)
print(m1)

print(m1.group())