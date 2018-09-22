#lamada用法
#以lambda 开头
# 紧跟一定的参数
#参数后用冒号和表达式主题隔开
#只是一个表达式，所以没有func
# 计算一个数字的100倍数
#
# stm = lambda x: 100*x
#
# #使用上跟函数一样
# #print(stm(98))
#
#
#
# stm2 = lambda x,y,z:x+y*10+z*20
# print(stm2(2,1,3))

## 高阶函数
# a = 10
# b = a
#
#
# #函数名就是一个变量
# def funA():
# 	print("qqqqq")
#
# funB = funA()
# print(funB)

##以上代码的得出结论： funA 和funB 只是名称不一样，既然函数变量名称是变量，则应该可以被当作参数传入另一个函数
##案例
# def funA(n):
# # 	return  n*100
# #
# # def funB(n):
# # 	return funA(n)*3
# #
# #
# # print(funB(9))
# #
# #
# # ##写一个高阶函数
# # def funC(n, f):
# # 	#假定函数可以扩大到100倍
# # 	return f(n)*3
# # print(funC(9,funA))

##系统高阶函数 -map
#愿意就是映射，即把集合或者列表的元素，每一个元素都按照一定规则进行操作，生成一个新的列表集合
#map函数就是系统提供的具体映射功能的函数，返回值是一个迭代的对象

# l1 = [i for i in range(10)]
# def mulTen(n):
# 	return  n*10
#
# l2 = map(mulTen,l1)
#
# print(l2)
# #map 是一个可迭代的结构，可以利用for循环
# for i in l2:
# 	print(i,end=" ")

##reduce
# 原意是归并，缩减
#把一个可迭代的对象最后归并成一个结果
#对于作为参数的函数要求，必须有两个参数，必须返回结果
#需要导入functools 包
# from  functools import reduce
#
# #d定义一个操作函数
# #加入操作函数只是相加
# def add(x, y):
# 	return  x+y
#
# rst = reduce(add,[1,2,3,4,5])
# print(rst)


##filter

#过滤函数，对一组数据进行过滤，符合条件的数据会生成一个新的列表
#跟map比较，
	#相同    都对列表的每一个元素逐一进行操作
	#不同    map会生成一个新的列表，与元数据相对应
			#filer不一定，只要符合条件的才会进入新的数据集合
	#filter函数怎么写：
	#利用函数给判断
	#需要定义过滤函数
	#过滤函数要求有输入，返回布尔值de
# def isEven(a):
# 	return a%2==0
#
# l = [1,2,3,4,5,6,7,8,10]
#
# rst = filter(isEven,l)
#
# print(rst)
#
# for i in rst:
# 	print(i)

#高阶函数排序

#把一个函数按照给定的算法进行排序
#key,

# a = [123,45,6,11,87,321]
# al = sorted(a,reverse=True)
# print(al)


# a = [123,45,6,11,87,321,-11]
#
# al = sorted(a,key=abs,reverse=True)
# print(al)
#
#
#


# astr = ['aa','nn','jhha','jjj']
#
# str1 = sorted(astr)
# print(str1)
#
# str2 = sorted(astr,key=str.lower)
# print(str2)



## 返回函数
def myF(a):
	print(" in my")
	return  None


a = myF(8)
print(a)