#print("你好")

#age = 19
##if age <18:
# '''
 #   print("去交作业吧")
#    print("hheh")
#print("开始上车咯")'''
#gender = input("please input sex: ")
#print("you input sex is {0}".format(gender))
#if gender == "man":
#    print("come somking")
#else:
#    print("cheat mill")#
#print("come to learning")

#列表 =打印列表中的值
#list = ['A','B','c']

#for name in list:
  #  if name =="c":
   #     print("i love {0}".format(name))
  #  else:
  #      print("not of you")


#生成数字序列 范围可以指定 range  (包含左边的数字，不包含右边的数字)

#for i in range(1,11):
#    print(i)

##循环之break；continue；pass

#for i in range(1,11):
#    if i == 7:
#        print("i find")
#        break
#    else:
#        print(i)

#for i in range(1,11):
#    if i % 2 == 1:
#        continue
#    else:
#        print("the number is {0}".format(i))

#while循环  条件成例就循环 如果说年利率是6.7% 。，则年后会是多少本钱  while-else

#bq = 100000
#years = 0
#while  bq<200000:
#    bq = bq * (1+0.067)
#    years += 1
#    print("第 {0} 年拿了{1}块钱".format(years,bq))

#else:
#    print("翻倍啦")

##函数   形式参数 实参
#def hello(person=""):
#    print("{0},你肿么咯呀".format(person))

#hello("leo")  print默认函数任务打印完毕后换行


#函数参数
#def jiujiu():
    # for i in range(1,10):
    #     for j in range(1, i + 1):
    #         print('{0}x{1}={2}\t'.format(i, j, i * j), end='')
        # print()

#jiujiu()

#形参带有默认值，#
#默认参数案例
# def reg(name,age,gender="man"):
#     if gender == "male":
#         print("{0}is {1} ,and he is a good student".format(name,age))
#     else:
#         print("{0}is {1} ,and she is a good student".format(name, age))
#
#
#
#
# reg("mingyue",12)


#关键字参数开始  使用关键字参数，不考虑参数位置

# def stu(name = "no name", age=0):
#     print("a student")
#     print("my name{0},i am {1} ".format(name,age))
#
# n = "ijijij"
# a = 13
#
# stu(age=a, name=n)

##收集参数
#模拟一个学生的自我介绍，具体内容不知道  args  把它看成一个列表

#收集参数不带任何参数，此时收集参数为tuple
# def stu(*args):
#     print("大家好啊")
#
#     print(type(args))
#
#
#     for i in args:
#         print(i)
#
#
#
# stu("leo",18,"anqing","no single")
#
# stu("lee",19,"maanshan")


##收集参数之关键字收集参数
#把关键字参数按照字典格式存入收集参数

#
#调用的时候把多余的关键字放入kwargs
# def stu(**args):
#     print("来说些啥之类的简述呢：")
#     print(type(args))
#     for k,v in args.items():
#         print(k, "---", v)
#
#
# stu(name="liuwenbing", age=19,addr="安徽马鞍山市",work="chengsux")
# print("*" * 20)
#
# stu()


##收集参数混合调用的问题  普通参数和关键字参数优先   顺序   普通参数-》关键字参数-》收集参数truple->搜集参数dict

#
# def stu(name, age, *args, hobby="没有",**kwargs):
#     print("hello  大家好")
#     print("我叫{0},{1}".format(name,age))
#     if hobby=="没有":
#         print("我没有爱好")
#     else:
#         print("我的爱好是{0}".format(hobby))
#
#     print("*"*20)
#
#     for i in args:
#         print(i)
#
#
#     print("*"*30)
#
#     for k,v in kwargs.items():
#         print(k,"---",v)
# name ="leo"
# age=19
#
# stu(name,age)
#
# stu(name,age,hobby="swiming")
#
# stu(name,age,hobby="swiming")


##函数文档

#文档查看-使用help函数。如 help(func)    s使用__doc__，推荐使用三字符串来定义
#
# def stu(name, age, *args):
#     '''
#     这是文档
#     saidna
#     sdlq;k
#     '''
#     print("This is hanshu ")
#
# print(help(stu))
#
# print(stu.__doc__)


##变量作用域
'''legb原则：
'''
# a1 = 100
# def fun():
#     print(a1)
#     print(" i am fun")
#     #a2
#     a2 = 99
#     print(a2)
# print(a1)
# print("*"*10)
# fun()



###提升局部变量为全局变量

#
# b1 = 100
# def fun():
#     global b1
#     b1 = 111
#     print(b1)
#     print(" i am fun")
#     #a2
#     b2 = 99
#     print(b2)
# print(b1)
# fun()

##globals locals 函数 可以通过显示局部变量 与全局变量
# a = 1
# b = 2
# def fun(c,d):
#     e=111
#     print("locals{0}".format(locals()))
#     print("globals{0}".format(globals()))
#
# fun(100,200)
###eval函数  把一个字符串当成一个表达式来执行，返回表达式执行后的结果

# x = 100
# y = 200
# z1 = x+y
# z2 = eval("x+y")
# print(z1)
# print(z2)


#exec
#注意字符串中引导的写法
# x = 100
# y = 200
# z1 = x+y
# z2 = exec("print('x+y:', x+y)")
# print(z1)
# print(z2)


##递归函数
#内置数据结构（变量类型）
#'''
#list set dict tuple
#'''
#list
  # 一组有顺序的序列集合

  #分片操作
  #注意截取的范围，左边包含下标值，右边不包含下标
  #下标志可以为空，如果不写，左边下标值默认为0,右边下标值为最大数加1,即表示截取到最后一个数据
# l1 = [1,2,3,4,5,6]
# print(l1[1:4])
# print(l1[:4])


#分片操作生成一个新的list
#n内置函数ID，负责显示或者数据的唯一确定编号
# a = 1
# b = 12
# print(id(a))
# print(id(b))
# #如果a跟c 只想显示一份数据。则更改a的值也会更改成c的值
#
# c =a
# print(id(c))
# print(c)
#
# a = 101
# print(a)
# print(c)

#from selenium import webdriver

#driver = webdriver.Chrome()
#driver.get("http://www.baidu.com")

# browser = webdriver.PhantomJS('/usr/local/phantomjs-2.1.1-macosx/bin/phantomjs')
# browser.get('https://www.baidu.com')
# print(browser.current_url)

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
#
# browser = webdriver.Chrome(chrome_options=chrome_options)
# browser.set_window_size(1400, 900)
# browser.get('https://www.baidu.com')
# print(browser.current_url)


# from bs4 import BeautifulSoup
#
# #soup = BeautifulSoup('<p>hello</p>','lxml')感觉弃用了
#
# soup = BeautifulSoup('<p>hello</p>','html.parser')
#
# print(soup.p.string)



# from  flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello():
# 	return  "hello world"
# if __name__ == "__main__":
# 	app.run()

##汉诺塔问题

#每次移动一个盘子。任何时候大盘子在下面小盘子在上面   n=1 直接移动到c盘子 a->c


# def hanNuoTa(n,a,b,c):
# 	'''
# 	:param n: 代表几个盘子
# 	:param a: 第一个
# 	:param b: 第二个
# 	:param c: 第三个
# 	'''
# 	if n== 1:
# 		print(a,'-->',c)
# 		return  None
# 	elif n == 2:
# 		print(a,'-->',b)
# 		print(a,'-->',c)
# 		print(b,'-->',c)
# 		return  None
# 	#把n-1个盘子，从a塔借助于c塔，挪到把b塔上去，
# 	hanNuoTa(n-1,a,c,b)
# 	print(a,'-->',c)
# # 把n-1个盘子，从b塔借助于a塔，挪到把c塔上去，
# 	hanNuoTa(n-1,b,a,c)
#
#
# a = "A"
# b = "B"
# c = "C"
# n = 3
# hanNuoTa(n,a,b,c)



##list 列表   如果删除之后id和以前的地址不一样，则说明删除生成了一个新的list
# a = [1,2,3,4,5]
# print(id(a))
# del a[2]
# print(id(a))
# print(a)
# #retrun
# 4571419848
# 4571419848
# [1, 2, 4, 5]

# 列表相加
# a  = [1,2,3,4,5]
# b =  [1,3,4,5,7]
#
# d  = ['q','w','r']
# c = a+ b+d
# print(c)
#
# [1, 2, 3, 4, 5, 1, 3, 4, 5, 7, 'q', 'w', 'r']

##成员资格运算   in / not in   return   boolean true /false
# a = [1,2,3,4,5]
# # b = 8
# # c = b in a
# # print(c)
# #


##链表的遍历 for  while
# a  =[1,2,3,4,5]
#
# for i in a:
# 	print(i)
# '''
# 	1
# 	2
# 	3
# 	4
# 	5
# '''

# b = ["i love liulin"]
# for i in b:
# 	print(i)
#
# i love liulin

#range   在in 后面的变量要求是可以迭代的   一般不用while 来作为循环list

# for i in range(1,11):
# 	print(i)
# print(type(range(1,11)))


## s双层循环列表变异
# a = [["one",1],["two",2]]
# for k,v in a:
# 	print(k,'--',v)
#
# one -- 1
# two -- 2

# a = [["one", 1,"eni"], ["two", 2,"wqq"]]
# for k, v ,w in a:
# 	print(k, '--', v,'--',w)
#
# one -- 1 -- eni
# two -- 2 -- wqq

#列表内涵

# a = [1,2,3,4]
# #用list a创建list b
# #b = [i for i in a]
# b = [i*10 for i in a]
# print(b)

#还可以过滤原来的list,中放入新的列表
# a = [x for x in range(1,35)]
#
# b = [m for m in a if m%2 == 0]
# print(b)
#
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]


##列表生成式也可以嵌套
# a = [i for i in range(1,4)]
# print(a)
# b = [i for i in range(100,400) if i%100 == 0]
# print(b)
#
#
# ##生成的列表可以嵌套
# c = [m+n for m in a for n in b]
#
# print(c)
# ##等价下面代码
# for m in a:
# 	for n in b:
# 		print(m+n,end=" ")
# print()


##列表的函数 len
# a  = [x for x in range(1,100)]
# print(len(a))
#
# #求最大值max
# print(max(a))
#
# b = ['man','flim','python']
# print(max(b))


#list 将其他格式的数据转转换成list
# a = [1,2,3]
# print(list(a))
# s = "i love liulin"
# print(list(s))
# print(list(range(12,19)))



##关于类的列表函数

##append 插入一个新的内容 末尾追加
#
# a = [i for i in range(1,5)]
# print(a)
# a.append(100)
# print(a)
#
# ##指定位置插入数据 插入位置index前面
# a.insert(3,900)
# print(a)
#
#
# ##删除
# # del删除  pop 从对位拿出一个元素，即最后一个元素取出来
# last_ele = a.pop()
# print(last_ele)
# print(a)
# [1, 2, 3, 4]
# [1, 2, 3, 4, 100]
# [1, 2, 3, 900, 4, 100]
# 100
# [1, 2, 3, 900, 4]


#remove :在列表中删除指定的值吃的元素  r如果删除的值不在list中，即删除的值操作使用try..except.则需要进行先判断
#输出俩个id一样的值，说明remove操作是在元list直接操作

#if x in list:   list.remove(x)

#clear清空

##清空列表方式
#
# print(a)
# print(id(a))
# a.remove(900)
# print(a)
# print(id(a))

###reverse     反转列表内容，原地反转

# a = [1,2,3,4,5]
# print(a)
# print(id(a))
# a.reverse()
# print(a)
# print(id(a))



##extend  扩展列表，2个列表，把一个直接拼接到最后一个上

# a = [1,2,3,4,5]
# b = [6,7,8,9]
# print(a)
# print(id(a))
#
# a.extend(b)
# print(a)
# print(id(a))


#查找列表中指定值或者元素的个数
# a  = [1,2,3,4,5]
# print(a)
# a.append(8)
# print(a)
# a_len = a.count(8)
# print(a_len)
#copy 拷贝
# a  = [1,2,3,4,5,666]
# print(a)
# #list类型，简单赋值  是传地址
# b  = a
# b[3] = 777
# print(id(a))
# print(a)
# print(id(b))
# print(b)
# print("*"*20)
# b = a.copy()
# print(id(a))
# print(a)
# print(id(b))
# print(b)
# print("*"*20)
# b[3] = 1000
# print(a)
# print(b)

##深度拷贝 浅度拷贝

# a = [1,2,3,[10,20,30]]
# b = a.copy()
# print(id(a))
# print(id(b))
# print(a)
# print(b)
# a[3][2] = 444
# print(a)
# print(b)

##一下情况属于浅拷贝，只拷贝一层

#
# '''
# 4338127048
# 4338088328
# [1, 2, 3, [10, 20, 30]]
# [1, 2, 3, [10, 20, 30]]
# [1, 2, 3, [10, 20, 444]]
# [1, 2, 3, [10, 20, 444]]
# '''

##深拷贝需要用到特定的工具


#### 元祖
#--是不可以更改操作的列表list
#元祖的创建\
# t = ()
# print(type(t))

##只创建一个值的元祖
# t = (1,)
# # # print(type(t))
# # # print(t)
# # #
# # # t = 1,
# # # print(type(t))
# # # print(t)
# # #
# # # '''<class 'tuple'>
# # # (1,)
# # # <class 'tuple'>
# # # (1,)'''

##创建多个
# t = (1,3,5,5)
# l = [1,2,3,4,5]
#
# print(t)
# t = tuple(l)
# print(t)

##y元祖的特性
#是序列表 有序  元祖数据值可以访问。不可能修改 元祖数据是可以任意的类型   总之，list所有的特性，除了可修改外，元祖都具有

#也就意味着list具有一些操作，比如索引，分片，序列相加，拼接

#索引操作
# t = (1,2,4,5,6)
# #print(t[5])
#
# t1 = t[1::2]
# print(id(t))
# print(id(t1))
# print(t1)
#
# #切片可以超标
# t2 = t[2:100]
# print(t2)

##相加
# t1 = (1,2,3)
# t2 = (4,5,6)
# print(id(t1))
# #传地址操作
# t1 = t1 + t2
# print(t1)
# print(id(t1))

##以上操作类似于
##相加
# t1 = (1,2,3)
# t2 = (2,3,4)
# t1[1] = 100
# TypeError: 'tuple' object does not support item assignment

## 相乘
# t1 = (1,2,3)
# t1 = t1*3
# print(t1)


#元祖遍历数据 --- for
#单层元祖遍历
# t = (1,2,3,4,"21","ewq","uui")
# for i in t:
# 	print(i,end=" ")
#
# 1 2 3 4 21 ewq uui
#双层元祖遍历
# t = ((1,2,3),(3,4,5),("21","ewq","uui"))
# #
# for i in t:
# 	print(i)
#
# for k,m,n in t:
# 	print(k,'--',m,'--',n)
#
# '''(1, 2, 3)
# (3, 4, 5)
# ('21', 'ewq', 'uui')
# 1 -- 2 -- 3
# 3 -- 4 -- 5
# 21 -- ewq -- uui'''

##元组的函数
#-len:
# t = (1,2,3,4,5)
# print(len(t))

#max  min

#转化或创建元祖
# l = [1,2,3,4,5]
# t1 = tuple(l)
# print(t1)
#count:计算出现的次数
# t = (1,2,3,4,5,3,4)
# print(t.count(3))
# print(t.index(2))
#元祖变量交换
# a = 1
# b = 2
# a,b = b,a
# print(a)
# print(b)

##集合-set
#-集合是高中数学的一个概念  -- 一堆确定无序唯一的数据，集合中每一个数据成为一个元素
#集合定义
# s = set()
# print(type(s))
# print(s)
# '''<class 'set'>
# set()'''
#大阔号一定要有值，否则就是定义个=一个dict
# d = {}
# print(type(d))
# print(d)
#
# '''<class 'dict'>
# {}'''

# s = {1,2,3,4}
# print(s){1, 2, 3, 4}

###集合的特征
#集合内数据无序，既无法使用索引和分片  集合内部数据元素具有唯一性，可以用来排除重复数据

#集合背部数据  str float tuple int 即内部数据可哈希数据
#集合的序列操作
#成员检测
#in not in
# s = {1,"love",4,"i",6,7,8,"wq"}
# print(s)

#集合的遍历操作
# s = {1,"love",4,"i",6,7,8,"wq"}
#
# for i in s:
# 	print(i,end=" ")

# 带有元祖集合的遍历、
# s = {(1,2,3),("i","love","u")}
# for k,m,n in s:
# 	print(k,'--',m,'--',n)
#
# for k in s:
# 	print(k)
#集合的内涵
# #普通的集合  =--g过滤重复数据
# s  = {1,2,4,5,6,100,8,1,999,6,8,0,7}
# #带条件的集合内涵
# # print(s)
# ss = {i for i in s if i%2==0}
# print(ss)

#
# s1 = {1,2,3,4}
# s2 = {"i","love","u"}
# s = {m*n for m in s2 for n in s1  if n==2}
# print(s)

#集合函数/关于集合的函数
#len max min
#set 生成一个集合
# l = [1,2,3,4,5]
# s = set(l)
# print(s)


# 集合内添加数据元素
# s ={1}
# s.add(22)
# print(s)
#clear  原地清空数据
#copy
#remove  指定的值   直接改变原有的值，如果要删除的值不存在，报错
#discard 移除集合中指定的值  跟remove一样。如果删除的话，不存在，不报错
#
# s = {23,4,12,100,1,2,3}
# s.remove(4)
# print(s)
# s.discard(1)
#
# print("*"*30)
#
# s.discard(1100)
# print(s)
# s.remove(1100)
# print(s)

#pop 随机移除一个元素

# s  = {1,2,4,5,6}
# d= s.pop()
# print(d)
# print(s)


##集合函数
#intersection 交集
#difference 差集
#· uinon   并集
# issubset  检查一个集合是不是子集
#issuperser 是否是超集
# s1 = {1,2,3,4,5,6}
# s2 = {5,6,7,8,9}
#
#
# s_1 = s1.intersection(s2)
# print(s_1)
# s_2 = s1.difference(s2)
# print(s_2)
# s_3 = s1.issubset(s2)
# print(s_3)

#集合的数学操作


#frozen set冰冻集合  是不可以进行修改的   s是一种特殊的集合
# s = frozenset()
# print(s)

#di字典  是一种组合的数据   没有顺序的组合数据，数据以键值对的形式出现
#字典的创建
# d = {}
# #d= dict()
# print(d)


#创建有值的字典，每一组数据都是用冒号隔开。，每一堆键值用逗号隔开
# d = {"noe":1,"two":2,"three":3}
# print(d)
# y有内容的字典
# d = dict({"noe":1,"two":2,"three":3})
# print(d)


#关键字参数
# d = dict(noe=1,two=2,three=3)
# print(d)
#
# d = dict([("one",1),("two",2),("three",3)])
# print(d)

#字典的特征
#字典是序列类型，但是是无序序列，所有没有分片，索引
#每个数据都有键值对，kv
#key · 必须保证可哈希  int float string tuple,但是list set dict不可以
###访问数据
# d = {"one":1,"teow":2}

# #访问括号内的键值
# print(d["one"])
#
# d["one"] ="enw"
# print(d)
#
# #删除del
# del(d["one"])
# print(d)

##成员检测  ---检测的是 key内容
# d = {"one":1,"teow":2}
#遍历数据  py2  不同 3

##直接被key访问
# for k in d:
# 	print(k,d[k])
#
# for k in d.keys():
# 	print(k,d[k])


#只访问字典的值
# for v in d.values():
# 	print(v)

#一下是特殊用法
# for k,v in d.items():
# 	print(k,"--",v)

##字典生成式
#d = {"one":1,"teow":2}

##常规
# dd = {k:v for k,v in d.items()}
# print(dd)



#j加限制条件的生成
# dd = {k:v for k,v in d.items() if v%2 ==0}
# print(dd)

##字典函数 len max min dict
#str 返回字典的字符串格式
#d = {"one":1,"teow":2}
# print(str(d))

#clear
#items   返回键值对组成的元组格式
# i = d.items()
# print(type(i))
# print(i)

# #keys 返回字典组成的一个结构
# i = d.keys()
# print(type(i))
# print(i)


#values 返回字典组成的一个结构
# i = d.values()
# # print(type(i))
# # print(i)

#get 根据定键返回相应的值，


#fromkeys  使用指定的序列作为键，使用一个值作为字典所有的键的值
# l = ["wwq","wq"]
# ##注意；formkeys2个参数的类型
# ##注意主体的调用
# d = dict.fromkeys(l,"enenenn")
# print(d)