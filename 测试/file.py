#打开文件
#r表示后面的字符串内容不需要转义
#f称之为文件句柄
# f =open(r"test.txt","w")
# f.close()

##with使用
#
# with open(r"test.txt",'r') as f:
# 	pass
# 	#下面语句块开始对文件进行f操作
# 	#在本模块中不需要在使用close关闭文件

##with案例
# with open(r"test.txt", 'r') as f:
# 	#按行读取内容
# 	strline = f.readline()
# 	#此结构保证能够读取文件直到结束
# 	while strline:
# 		print(strline)
# 		strline = f.readline()

#list能打开文件作为参数，把文件内每一行内容作为一个元素
# with open(r"tets.txt", 'r') as f:
# 	#以f作为参数创建列表
# 	l = list(f)
# 	for i in l:
# 		print(i)

#read是按照字符读取文件内容
#允许输入参数决定读取几个字符，如果没有指定，从当前位置读取到结尾
#否则，从当前位置读取指定个数字符

# with open(r"tets.txt", 'r') as f:
# 	strChar = f.read()
# 	print(len(strChar))
# 	print(strChar)
#
##seek（offset，from ）
#移动文件的读取位置，也叫做读取指针
#from的取值范围
# #seek案例  打开文件之后，从第五个字符开始读取
##

# with open(r"tets.txt", 'r') as f:
# # 	f.seek(6,0)
# # 	strChar = f.read()
# # 	print(strChar)

# import time
# with open(r"tets.txt", 'r') as f:
# 	#read参数可以理解成一个汉字一个字符
# 	strChar = f.read(3)
# 	while strChar:
# 		print(strChar)
# 		time.sleep(1)
# 		strChar = f.read(3)


#tell函数，显示文件当前的位置
# with open(r"tets.txt", 'r') as f:
# 	strChar = f.read(3)
#
# 	pos = f.tell()
#
# 	while strChar:
# 		print(pos)
# 		print(strChar)
# 		strChar = f.read(3)
# 		pos = f.tell()

#tell返回的字节，不是自字符
##文件的操作-write
#write(str) 把字符写入文件
#writelines(str)把字符串写入文件
#区别：一个是字符串，一个即是字符串也可以是序列

#write案例
# with open(r"tets.txt", 'r') as f:
# 	f.write("适合和，\n 还有远方的诗")
#序列化

#import pickle
# age = 19
# with open(r"test.txt", 'wb') as f:
# 	pickle.dump(age,f)

#反序列化
# age = 19
# with open(r"test.txt", 'rb') as f:
# 	age = pickle.load(f)
# 	print(age)

#使用shelve
import  shelve
# shv = shelve.open(r'shv.db')
# shv['one'] = 1
# shv['two'] = 2
#
# shv.close()

#shv读取
#
# shv = shelve.open(r'shv.db')
# try:
# 	print(shv['one'])
# except Exception as e:
# 	print("eqwewq")
# finally:
# 	shv.close()