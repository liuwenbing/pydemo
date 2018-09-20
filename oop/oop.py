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



##属性案例
##创建student类，描述学生，
##可以增加一个
# class Student():
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
#
# 		#如果不想修改代码
# 		self.setName(name)
#
# 	#介绍自己
# 	def info(self):
# 		print(" hai , my name is {}".format(self.name))
# 	def setName(self,name):
# 		self.name = name.upper()
#
# s1 = Student("Liu",19)
# s2 = Student("mii",30)
#
# s1.info()
# s2.info()

##属性案例-property
#定义一个person类，具有name age属性
#pproperty
# class Person():
# 	def fget(self):
# 		return  self._name *2
#
# 	def fset(self,name):
# 		self._name =  name.upper()
#
# 	def fdel(self):
# 		self._name = "NOname"
#
# 	name = property(fget,fset,fdel,"对name操作")
#
# p1 = Person()
#
# p1.name ="tulin"
#
# print(p1.name)

##类的内置属性

# class Person():
# 	def fget(self):
# 		return  self._name *2
#
# 	def fset(self,name):
# 		self._name =  name.upper()
#
# 	def fdel(self):
# 		self._name = "NOname"
#
# 	name = property(fget,fset,fdel,"对name操作")
#
# p1 = Person()
#
#
# print(Person.__dict__)
# print(Person.__doc__)
# print(Person.__name__)
# print(Person.__bases__)

##魔术方法

# class A():
# 	def __init__(self,name=0):
# 		print("我被调用")
#
#
# a = A()
#
# print(a)

##__call__
# class A():
# 	def __init__(self,name=0):
# 		print("我被调用")
#
# 	def __call__(self):
# 		print("我又被调用了")
# a = A()
# ##函数当作实例调用
# a()

##__str_
#
# class A():
# 	def __init__(self,name=0):
# 		print("我被调用")
#
# 	def __call__(self):
# 		print("我又被调用了")
#
# 	def __str__(self):
# 		return  "uhuhuhu"
#
#
#
# a = A()
#
# print(a)

##__getattr


# class A():
#
# 	name="qq"
# 	age = 12
# 	def __getattr__(self, name):
# 		print("我被调用")
# 		print(name)
#
# a = A()
# print(a.name)
# print(a.addr)


###__asetattr__
# class Person():
# 	def __init__(self):
# 		pass
# 	def __setattr__(self, name, value):
# 		print("没有设置属性 {0}".format(name))
#
# 		#下面一句话会导致死循环
# 		###self.name = value
#
# 	##为避免死循环，操作方法，规定调用父类魔术函数
# 		super().__setattr__(name,value)

#
#
#
# p = Person()
# print(p.__dict__)
# p.age = 18



##__gt__

# class Student():
# # 	def __init__(self,name):
# # 		self.name = name
# #
# # 	def __gt__(self, obj):
# # 		print("哈哈，{0} 比 {1} 大吗？".format(self,obj))
# # 		return self._name > self._name
# #
# #
# # stu1 = Student("one")
# # stu2 = Student("two")
# #
# # print(stu1>stu2)


##三种方法案例

# class Person():
# 	#实例化方法
# 	def eat(self):
# 		print(self)
# 		print("eating...")
# 	#类方法
# 	#类方法的第一个参数，一般会命名cls，区别于self
# 	@classmethod
# 	def play(cls):
# 		print(cls)
# 		print("clsing.....")
# 	#静态方法，没有参数
# 	#不需要第一个参数表示自身
# 	@staticmethod
# 	def say():
# 		print("say,,...")
#
#
# yue = Person()
# #实例方法
# yue.eat()
# #类方法
# yue.play()
# #静态方法
# yue.say()


#变量的三种方法
# class A():
# 	def __init__(self):
# 		self.name = "fafa"
# 		self.age = 19
#
# a =A()
#
# #类的三种当法  赋值 读取  删除
# a.name = "liu"
# print(a.name)

# 类属性 property
# 对变量除了普通三种操作，还想增加一些附加操作，name可以通过property完成

# class A():
# 	def __init__(self):
# 		self.name = "fafa"
# 		self.age = 19
#
# 	# 模拟的是对变量进行读取操作的时候执行功能
#
# 	def fget(self):
# 		print("我读取了")
# 		return  self.name
# 	# 模拟的是对变量进行写操作的时候完成的功能
# 	def fset(self,name):
# 		print("我被磕=写入了")
# 		self.name = "tulin" +name
# 	#进行的是删除操作
# 	def fdel(self):
# 		pass
# 	#property的四个参数位置是固定的
# 	#第一个参数代表读取
# 	#第二个代表写入
# 	#第三个代表删除
# 	name2 = property(fget,fset,fdel,"这是一个property的例子")
# a =A()
# #print(a.name)
# print(a.name2)
#


##抽象方法
# class Animal():
# 	#
# 	def sayHello(self):
# 		pass
#
#
# class Dog(Animal):
# 	def sayHello(self):
#
# 		print("闻一下")
#
# class Person(Animal):
# 	def sayHello(self):
#
# 		print("kiss me")
# d = Dog()
# d.sayHello()
#
# p = Person()
# p.sayHello()


#抽象类实现
# import  abc
# # #声明一个类并且指定当前类的元素
# # class Human(metaclass=abc.ABCMeta):
# #
# # 	# d定定义类的抽象方法
# # 	@abc.abstractmethod
# # 	def drink(self):
# # 		pass
# # 	#定义抽象方法
# # 	@abc.abstractclassmethod
# # 	def smoking(cls):
# # 		pass
# #
# # 	#定义静态方法
# # 	@abc.abstractstaticmethod
# # 	def work():
# # 		pass
# # 	def sleep(self):
# # 		print("smoking....")



## h函数名当作变量来用
# def sayHello(name):
# 	print("hello {0} ,可以来一发吗？".format(name))
# sayHello("yueyu")
# lium = sayHello
# lium("ll")


##自己组装一个类
# class A():
# 	pass
# 	def say(self):
# 		print("saying...")
#
# 	say(9)
#
# a = A()
# A.say =say

# from types import MethodType
# class A():
# 	pass
# def say(self):
# 		print("saying...")
#
#
# a = A()
# a.say =MethodType(say ,A)
# a.say()
#
# help(type)

##利用type造一个类
#
# def say(self):
# 	print("saying...")
#
# def talk(self):
# 	print("talking...")
#
# #zaolei
#
# A = type("AName",(object, ),{"class_say":say,"class_talk":talk})
#
#
# a  =A()
#
#
# a.class_say


##元类演示、

#元类是固定的，必须继承type
#一般是命名TulinMetaClass结尾
#
# class TulinMetaClass(type):
# 	#注意一下写法
# 	def __new__(cls, name, bases,attrs):
# 		#自己的业务代码
# 		print("哈哈哈")
# 		attrs['id'] = 1
# 		attrs['addr'] ="ajdahi"
# 		return  type.__new__(cls,name,bases,attrs)
#
# #元类定义玩就可以使用，
# class Teacher(object,metaclass=TulinMetaClass):
# 	pass
# t = Teacher()
#
# t.__dict__
# print(t.id)