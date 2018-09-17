# '''
# 定义一个学生类
# '''
# #定义一个空的类
# class Student():
# 	#一个空类  此次pass必须有  pass代表跳过
# 	pass
# #定义一个对象
# migyue = Student()
#
# #定义一个听python的类
# class PythonStident():
# 	#用none给不确定的值赋值
# 	name = None
#
# 	age = 18
# 	course = "Python"
#
# 	#注意  def doHomeWork 缩紧层级   系统默认self参数
# 	def doHomeWork(self):
# 		print("在做作业")
# 		#推荐在函数末尾使用return
# 		return  None
#
# #实例话月月的学生，是具体的一个人
# yueyue = PythonStident()
# print(yueyue.name)
# print(yueyue.age)
# #注意成员函数的调用没有传递进入参数
# yueyue.doHomeWork()

#
# class A():
# 	name ="Dada"
# 	age = 18
#
# 	def say(self):
# 		self.name = "ddd"
# 		self.age  = 10
# 	#此案例说明
# 	#类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，
# 	#指向同一个变量
# 	#此时，A称为类实例
# print(A.name)
# print(A.age)
# print("*"*20)
# #id 可以鉴别一个变量是否和另一个变量是同一个变量
# print(id(A.name))
# print(id(A.age))
# print("*"*20)
#
# a  = A()
# print(a.name)
# print(a.age)
# print(id(a.name))
# print(id(a.age))
# print("*"*20)
# a.name = "@132"
# a.age  = 22
#
# print(a.name)
# print(a.age)
#
# print(id(a.name))
# print(id(a.age))


##self
# class Student():
# 
# 	name = "das"
# 	age  = 23
# 	def say(self):
# 		self.name = "leo"
# 		self.age = 33
# 		print("My name is {0}".format(self.name))
# 		print("i am {0}".format(self.age))
# 
# yueyue = Student()
# yueyue.say()

# class Teacher():
# 	name = "eqeq"
# 	age = 34
# 	def say(self):
# 		self.name = "yyy"
# 		self.age  = 88
# 		print("My name is {0}".format(self.name))
# 		print("i am {0}".format(self.age))
#
#
# 	def sayAgain():
# 		print(__class__.name)
# 		print(__class__.age)
# 		print("hello，see有aga")
#
# t = Teacher()
#
# t.say()
# #调用绑定当法类函数使用类名
# Teacher.sayAgain()


#关于self的案例
# class A():
# 	name = "liuwen"
# 	ahe = 12
#
# 	def __init__(self):
# 		self.name = "ooo"
# 		self.age = 44
#
# 	def say(self):
# 		print(self.name)
# 		print(self.age)
# class B():
# 	name = "ggg"
# 	age = 999
#
# a = A()
# #此时，系统会默认把a作为第一个参数传入函数
# a.say()
#
# #此时。self会被a替换
# A.say(a)
#
# #同样可以把A作为参数传入
# A.say(A)
# #此时，传入的是类的实例B，因为具有name和age属性，所以不会报错
# #A.say(B)

##私有变量
class Person():
	name = "liu" #公有
	#—__age私有、
	__age = 12

p = Person()
print(p.name)

p.Person__age = 18
print(p.Person__age)