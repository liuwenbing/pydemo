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
# class Person():
# 	name = "liu" #公有
# 	#—__age私有、
# 	__age = 12
#
# p = Person()
# print(p.name)
#
# p.Person__age = 18
# print(p.Person__age)

##类继承的语法

##子类和父类同一个名称，优先使用子类的
# class Person():
# 	name = "human"
# 	__age = 18
# 	__score = 0      #私有的
# 	_petname = "sec" #小名受保护的。不可以公有
# 	def sleep(self):
# 		print("sleep...")
#
# #父类写在括号内
# class Teacher(Person):
# 	teacher_id = "111"
# 	name = "hh"
# 	def make_test(self):
# 		print("do test")
#
#
#
# t = Teacher()
# print(t.name)
#
# #print(Teacher.name)
#
# print(t._petname)
# print(t.teacher_id)
# t.make_test()

##公开访问私有会报错
#print(t.__score)


#子类扩充父类功能

# class Person():
# 	name = "human"
# 	__age = 18
# 	__score = 0  # 私有的
# 	_petname = "sec"  # 小名受保护的。不可以公有
#
# 	def sleep(self):
# 		print("sleep...")
# 	def work(self):
# 		print("make money..")
#
#
#
# # 父类写在括号内
# class Teacher(Person):
# 	teacher_id = "111"
# 	name = "hh"
#
# 	def make_test(self):
# 		print("attention")
#
# 	def work(self):
# 		#扩充父类的功能，只需调用父类相应的函数  1
# 		#Person.work(self)
# 		#super代表得到父类   2
# 		super().work()
# 		self.make_test()
#
# t = Teacher()
#
# t.work()
#
#make money..
#attention


##构造函数类
# class Dog():
# 	##__init__就是构造函数
# 	#每次实例化的时候，第一个被调用
# 	#因为主要工作是进行初始化，所以得名
# 	def __init__(self):
# 		print("i an aaa")
#
#
#
# 实例化的时候括号内的参数需要很构造函数以牙膏
# kaka = Dog()


##继承中的构造函数

# class Animal():
# 	def __init__(self):
# 		print("animals")
#
# class Paxin(Animal):
# 	pass
#
# class Dog(Paxin):
# 	##__init__就是构造函数
# 	#每次实例化的时候，第一个被调用
# 	#因为主要工作是进行初始化，所以得名
# 	def __init__(self):
# 		print("i an aaa")
#
#
#
# #实例话的时候，自动调用dog的构造函数
# #因为找到构造函数，则不在查找父类的构造函数
# kaka = Dog()

#
# class Mao(Paxin):
# 	pass
#
# #此时应该自动调用爬行的构造函数
#
# c = Mao()


##
#
# class Animal():
# 	def __init__(self):
# 		print("animals")
#
# class Paxin(Animal):
# 	def __init__(self,name):
# 		print("paxing dongwu {0}".format(name))
#
# class Dog(Paxin):
# 	##__init__就是构造函数
# 	#每次实例化的时候，第一个被调用
# 	#因为主要工作是进行初始化，所以得名
# 	def __init__(self):
# 		print("i an aaa")
#
#
#
# #实例话的时候，自动调用dog的构造函数.
# kaka = Dog()
#


#此时应该自动调用爬行的构造函数

## 因为paxin需要构造2个参数，实例话只给了一个，会报错
# class Mao(Paxin):
# 	def __init__(self):
# 		pass
#
# c = Mao()




##SQewqewqewqew

##单继承 多继承
#子类可以拥有父类的属性和方法，私有除外
# class Fish():
# 	def __init__(self,name):
# 		self.name = name
# 	def swim(self):
# 		print("i am swim")
#
# class Bird():
# 	def __init__(self,name):
# 		self.name = name
# 	def fly(self):
# 		print("i am fly")
#
# class Person():
# 	def __init__(self, name):
# 		self.name = name
#
# 	def work(self):
# 		print("i am work")
#
# class SuperMan(Person,Bird,Fish):
# 	def __init__(self, name):
#		self.name = name



# yue = SuperMan("yuyu")
# yue.fly()
# yue.swim()

# 构造函数
# class Person():
# 	def __init__(self):
# 		self.name = "qqq"
# 		self.age  = 18
# 		self.address ="anjui"
# 		print("in init func")
#
# #实例化一个人
# a = Person()
# print(a.name)

##构造函数的调用顺序，子类没有构造函数，自动向上查找
##此时会出现参数错误
# class A():
# 	def __init__(self):
# 		print("AAAA")
#
# class B(A):
# 	def __init__(self,name):
# 		self.name = name
# 		print("B")
#
# class C(B):
# 	pass
#
#
# c = C()
# print(c)

##构造函数3
#
# class A():
# 	def __init__(self):
# 		print("AAAA")
#
# class B(A):
# 	def __init__(self,name):
# 		self.name = name
# 		print("B")
#
# class C(B):
	##c想扩展b的构造函数，即在B的构造函数后添加一些功能
	##由2种方法
	##第一种是通过父类名调用
	# def __init__(self,name):
	# 	#首先调用父类函数
	# 	B.__init__(self,name)
	# 	#其次添加自己的功能
	# 	print("c中附加的功能")

# 	#第二种
# 	def __init__(self,name):
# 		super(C,self).__init__(name)
#
# 	print("c中附加的功能")
#
#
#
# c = C("wo")
# print(c)


##MIxin案例
#
# class Person():
# 	name = "aa"
# 	age = 18
# 	def eat(self):
# 		print("eat...")
# 	def drink(self):
# 		print("drink...")
# 	def sleep(self):
# 		print("sleep...")
#
#
# class Teacher(Person):
# 	def work(self):
# 		print("work...")
# class Student(Person):
# 	def study(self):
# 		print("study..")
#
# class Turto(Teacher,Student):
# 	pass
#
# t = Turto()
#
# print(Turto.__mro__)
#
# print(t.__dict__)
# print(Turto.__dict__)
#
# print("*"*30)
#
# class TeacherMixin():
# 	def work(self):
# 		print("work .....")
#
# class StudentMixin():
# 	def study(self):
# 		print("study..")
#
# class TurtorMixin(Person,TeacherMixin,StudentMixin):
# 	pass
#
# tt  =TeacherMixin()
# print(TurtorMixin.__mro__)
# print(tt.__dict__)
# print(TurtorMixin.__dict__)
#


#issubclass
# class A():
# 	pass
#
# class B(A):
# 	pass
#
# class C():
# 	pass
#
#
#
# print(issubclass(B,A))
#
# print(issubclass(C,A))
#
# print(issubclass(C,object))

#isinstance
#
# class A():
# 	pass
#
# a = A()
#
# print(isinstance(a,A))
#
# print(isinstance(A,A))

#hassttr

# class A():
# 	name ="33"
#
#
# a = A()
#
# print(hasattr(a,"name"))
#
# print(hasattr(a,"age"))



