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
# def myF(a):
# 	print(" in my")
# 	return  None
#
#
# a = myF(8)
# print(a)

#负责一点的返回函数 的例子
#args :参数列表
#1,myf4定义函数，返回内部定义的函数myf5
#2myf5使用类外部变量，这个变量是myf4 的参数
# def myF4( *args):
# 	def myF5():
# 		rst =0
# 		for n in args:
# 			rst +=n
# 		return rst
# 	return myF5
#
# f5 = myF4(1,2,3,4,5,6,7)
# #f5的调用方式
# print(f5())


##闭包（closure)
#当一个函数在内部定义函数，并且内部的函数应用外部函数的参数
#或者局部变量，当内部函数被当作返回值的时候，相关参数和变量
#保存在返回的函数中，这种结果，叫做闭包
#上面定义的myf4是一个标准的闭包结构
#闭包常见的坑

# def count():
# 	#定义列表,列表中存放的死定义的函数
# 	fs = []
# 	for i in range(1,4):
# 		#定义一个函数
# 		def f():
# 			return  i*i
# 		fs.append(f)
# 	return  fs


# ##装饰器
# def hello():
# 	print("hello world")
#
#
# #hello()
# p= hello
# p()

##现在的新需求，
#对hello功能进行扩展，每次打印hello之前打印当前的系统时间
#而实现这个功能又不能改动现有的代码



###装饰器
#再不改动函数代码的基础上无限制扩展函数的一种机制，装饰器是一个返沪函数的高阶函数
#装饰器的作用，使用@语法，即在内茨要扩展到函数定义之前使用@+函数名


# import  time
# #高阶函数
# def prinTime(f):
# 	def wraper(*args, **kwargs):
# 		print("time:" ,time.ctime())
# 		return f(*args, **kwargs)
# 	return wraper
#
# ##上面定义类装饰器，使用的时候需要用到@，词符号是python的语法糖
# @prinTime
# def hello():
# 	print("hello world")
#
# hello()


##装饰器的好处是，一点定义则可以装饰任意函数
#一旦被其装饰，则把装饰器的功能直接添加到定义函数的功能上
# @prinTime
# def hello2():
# 	print("我还有很多")
# 	print("还有很多选择")
#
# hello2()
#
#
# ##上面的函数使用类系统定义的语法糖
# #下面开始动手执行下装饰器
# #先定义函数
# def hello3():
# 	print("我是手动的饿")
#
# hello3()
#
# hello3 = prinTime(hello3)
# hello3()

##偏函数
 #把字符串转化为十进制
print(int("12346"))


