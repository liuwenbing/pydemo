
def sayHello(name):
		print(" i want say hello with you,{0}".format(name))
		print("hello ,{0}".format(name))
		print("done.....")

#此判断语句建议一直作为程序的入口
if __name__ == '__main___':
	print("**"*10)
	name = input("please input you anme:")
	print(sayHello(name=name))
	print("@@@@"*10)
