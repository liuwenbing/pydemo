#需要借助importlib包可以实现导入以数字开头的模块名称

import  importlib
#相当于导入类一个叫01 的模块
tulin = importlib.import_module("01")
stu = tulin.Student()
