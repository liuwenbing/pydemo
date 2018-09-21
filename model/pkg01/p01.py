#包含一个学生类
#一个say hello函数

class Student():
	def __init__(self,name="Noname",age=18):
		self.age = age
		self.name = name

	def say(self):
		print("my name is {0}".format(self.name))



def sayHello():
		print("Hi welcome")


print("heool")

