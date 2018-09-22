#import  calendar
#获取日历日期-一年
#cal = calendar.calendar(2017)
#print(cal)

# cal =calendar.calendar(2017,l=0,c=5)
# print(cal)
#isleap 获取某一年是否为闰年
#
# print(calendar.isleap(2000))
#
#
# #leapdays ：获取指定年份之间的闰年个数
# print(calendar.leapdays(2001,2018))

# help(calendar.leapdays)

##获取某个月的日历字符串month()

#w,t= calendar.monthrange(2018,3)

#获取一个月的周几开始monthrange
#elp(calendar.monthrange)

#monthcalendar返回一个月每天的矩阵列表
# m = calendar.monthcalendar(2018,3)
# print(m)

#prcal  打印日历

# print(calendar.prcal(2018))

#prmonth  打印yue日历

# print(calendar.prmonth(2018,3))

#weekday  获取周几

# print(calendar.weekday(2018,3,26))

###time模块

#import  time
#打印当前

#timezone:当前时区和utc时间相差的秒数，
#altzone:
#daylight
#print(time.daylight)


#
#localtime 得到当前时间结构
# print(time.time())
# t= time.localtime()
# # print(t.tm_hour)
#
# tt = time.asctime(t)
#
# print(tt)


#ctime  :获取字符串化的时间
# t = time.ctime()
# print(t)


##mktime()使用时间元祖获取对应的时间戳
# lt = time.localtime()
# ts = time.mktime(lt)
#
# print(ts)


#clock   获取cpu时间


#sleep 使进程进入睡眠,n秒后继续
# for i in range(1,9):
# 	print(i)
# 	time.sleep(1)

# def p():
# 	time.sleep(2.5)
# t0 = time.clock()
# p()
# time.sleep(3)
# t1 = time.clock()
#
# print(t1-t0)

##strftime  将时间元祖转化为自定义的字符串格式


##时间表示成 2018 3。26 21：10

# t = time.localtime()
# # ft = time.strftime("%Y年%m月%d日 %H:%M" , t)
# # print(ft)

##datetime模块

#import  datetime

#常见属性
#datetime.date
#提供日期跟时间的组合
# dt  = datetime.date(2018,9,22)
# print(dt)
#
# print(dt.day)
# print(dt.year)
# print(dt.month)

#提供日期跟时间的组合
#from datetime import datetime
#today
#now
#utcnow
#fromtimestamp

# dt = datetime(2018,9,22)
#
# print(dt.today())
# print(dt.now())
#
# print(dt.fromtimestamp(time.time()))


# from datetime import datetime, timedelta
#
# t1 = datetime.now()
# print(t1.strftime("%Y-%m-%d %H:%M:%S"))
# #td表示以小时的时间长度
# td = timedelta(hours=1)
# #当前时间加上时间间隔后，格式化的时间输出
# print((td+t1).strftime("%Y-%m-%d %H:%M:%S"))


#timeit  时间测量工具
# import  time
#
# def p():
# 	time.sleep(3.6)
# t1 = time.time()
#
# p()
#
# print(time.time()-t1)

##生成列表两种比较方法

# from datetime import datetime as dt
# print(dt.now())

#os

#getcwd()
#返回值，当前的工作目录字符串
#import  os
#mydir = os.getcwd()
# print(mydir)
#chdir
#改变当前的工作目录
# os.chdir('/Library/WebServer/pydemo')
# mydir = os.getcwd()
# print(mydir)

#listdir 获取一个目录中所有子目录和文件名称的列表
# ld = os.listdir()
#
# for i in ld:
#
# 	print(i)

##makedirs 创建一个文件夹
##当前目录下创建一个dana文件夹
# rst = os.makedirs("dana")
# print(rst)

#system  运行系统shell命令
#
# rst = os.system('rm -rf dana')
# print(rst)

#getnev()  h获取系统指定的环境变量值
# rst = os.getenv("PATH")
# print(rst)

#exit()  退出当前程序


#

# print(os.pardir)
# print(os.curdir)
# print(os.sep)
# print(os.linesep)
# print(os.name)

#os.path模块
#abspath

#import  os.path as op
# absp = op.abspath(".")
# print(absp)

#basename  获取路径的文件名
# bn = op.basename("/Library/WebServer/pydemo/model")
# print(bn)

#join 将多个路径拼成一个路径

#split 将路径切割成为文件夹部分和当前文件部分
# print(d,p)
# t= op.split("/Library/WebServer/pydemo/model/model.py")
# print(t)
#
# d,p = op.split("/Library/WebServer/pydemo/model/model.py")


#isdir  检测是否目录、
# rst = op.isdir("/Library/WebServer/pydemo/model/model.py")
# print(rst)

#exists  检测文件或这目录是否存在
# e= op.exists("//Library/WebServer/pydemo/a")
#
# print(e)

#shuilt  模块
#copy
#格式 shuilt.copy


import shutil

# copy2()

#copyfile  将一个文件的内容复制到另外一个文件中

#move 移动文件夹/文件

#归档和压缩
#make_archive (归档操作# )

