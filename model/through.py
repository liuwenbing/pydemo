#
# #j简单异常实例
# #给出提示信息
# #越具体越靠前
# try:
# 	num = int(input("input your num:"))
#
# 	rst = 100/num
# 	print("计算结果是：{0}".format(rst))
#
# #捕获异常后，把异常实例化，出错信息在实例里
# #注意一下写法
# #一下捕获语句是ZeroDivisionError异常并且实例化e
# except ZeroDivisionError as e:
# 	print("你他娘的啥玩意啊")
# 	print(e)
# 	#exit 是推出程序
# 	exit()
# except NameError as e:
# 	print("name error")
# 	print(e)
# 	exit()
# except ArithmeticError as e:
# 	print("attr error")
# 	print(e)
# 	exit()
#
# #所有的异常都是Exception的子类，任何异常都会截住
# #而且，下面这句话一定是exception。顺序很重要
# except Exception as e:
# 	print(" i dont no where error")
# 	exit()

##raise异常
# try:
# 	print("i love liuliu")
# 	print(3233.323)
#
# 	raise ValueError
# 	print("还没完呢")
# except NameError as e:
# 	print("name error")
# 	exit()
# except ValueError as e:
# 	print("valeu error")
# 	exit()
# except Exception as e:
# 	print("error")
# 	exit()
# finally:
# 	print("end")


##raise异常2
#
# class DanaError(ValueError):
# 	pass
#
#
# try:
# 	print("i love liuliu")
# 	print(3233.323)
#
# 	raise DanaError
# 	print("还没完呢")
# except NameError as e:
# 	print("name error")
# 	exit()
# except ValueError as e:
# 	print("valeu error")
# 	exit()
# except Exception as e:
# 	print("error")
# 	exit()
# finally:
# 	print("end")

##else语句

try:
	num = int(input("input your num:"))

	rst = 100/num
	print("计算结果是：{0}".format(rst))

#捕获异常后，把异常实例化，出错信息在实例里
#注意一下写法
#一下捕获语句是ZeroDivisionError异常并且实例化e
except Exception as e:
	print("error")
	exit()
else:
	print("no except")
finally:
	print("我亲亲我")