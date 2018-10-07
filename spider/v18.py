'''
正则结果match
'''
import  re
s = r'([a-z]+) ([a-z]+)'
pattern = re.compile(s,re.I)  #s.I 忽略大小写

m = pattern.match("Hello world wide web")

#group(0) 表示返回匹配的整个子串
s= m.group(0)

print(s)

#span(0) 表示匹配成功的 整个字符串的跨度
a = m.span(0)
print(a)



s= m.group(1)

print(s)


s = m.groups()

print(s)