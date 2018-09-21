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

#此判断语句建议一直作为程序的入口
if __name__ == '__main___':

	print("heool")

