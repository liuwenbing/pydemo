#1 模块

- 一个模块就是包含python代码的文件，后缀名就是.py就可以，模块就是个python文件
- 为什么我们要用模块啊
    - 程序太大，编写维护不方便
    - 模块可以增加代码重复利用的方式
    - 当作命名空间的使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通问价，所以任何代码可以直接写
    - 不过根据模块的规范，最好在本模块中编写一下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
- 如何使用模块
  - 模块直接倒入
    - 假如模块名称直接以数字为开头，需要借助于importlib
  - 语法
        import model_name
        model_name.function_name
        model_name.class_name
        
  - 案例 01 02 
  - import 模块 as 别名
    - 导入的同时给模块起一个别名,不需要前缀
    - 其余用法一样
    - 案例04

  - from model_name import *
    - 导入模块所有内容
    - 案例05
    
- if __name__ == '__main___':的使用
    - 可以有效解决避免模块代码被导入的时候被动执行的问题
    - 建议所有程序的入口代码都以此代码为入口
#2. 模块的搜索路径与存储
- 什么是模块的搜索路径
    - 加载模块的时候，系统会在那些地方寻找此模块
- 系统默认的搜索路径
    -import sys
        sys.path
        #案例06
        
- 添加搜索路径
    -   sys.path.append(dir)
- 模块的加载顺序
    1。上搜索内存中已经加载好的模块
    2。搜索  python的内置模块
    3。 搜索sys.path 路径
    
#3 包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包

- 自定义包的结构
                             
- 包的导入操作
    - import package_name
           - 直接导入一个包，可以用__init__.py中的内容
           - 使用方式：
                package_name.func_name
                package_name.class_name.func_name()
           - 此中方式的访问内容
           - 案例pkg01    07
           
    - import package_name as 别名（p）
        - 使用方法跟上序一样
        - 注意的是此种方法是默认对 __init__.py内容的导入
    - import package.module                
        - 导入包中具体模块
        - 使用方法
            package.module.func_name
            package.module.class.fun()
            package.module.class.var   
        - 案例 p08.py  
        
    -  import package.module s pm
    
- from ... import 导入
    - from package import module,....
    - 此中方法不执行__init__   
        - from pkg01 import p01
          p01.sayHello()
          
    - from package import *
    
        - 导入当前包    __init__.py  文件中的所有函数和类
        
        - 使用方法
            -func_name()
            -class_name.func_name()
            -class_name.var
        - 案例09      
- from package.module import *
    - 导入包中指定的所有内容
    -使用方法
        - func_name()
        - class_name.func_name()
        
- 在开发环境中经常会使用其他模块，可以在当前包中直接导入其他模块的内容
    -   import 完整的包或者模块的路径
- '__all__'的用法
    - 在使用 from package import * 的时候可以导入的内容  
    - __init__ 中如果文件为空，或者没有__all__，那么只可以把 __init__ 
    
    - __all__=['model1,2...']
    
    
# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定的前缀
- 作用是防止命名冲突
    - setName()
      Student.setName()   
      
      
      
# 常用模块
- calendar
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- string
- 上述所有模块使用理论上都应先导入

##calendar 
-使用先导入

# time 模块
### 时间戳
    - 一个时间表示，根据不同语言，可以是整数或者浮点数
    - 是从1970，，，经历的秒数
    - 太遥远可能出现异常
    - 32为操作系统，支持到2038年
###utc时间
    - utc时间称为世界协调时间
###夏令时

###时间元组
    -一个包含时间内容的普通元组    
##datetime模块
-datetime提供日期和时间的运算和表示


#datetime.datetime
- 查手册

#os-操作系统相关
    - os 系统相关目录 
    - os.path系统相关路径
    - shutil 高级文件操作，目录树的曹祖哦，文件赋值，删除，移动
    
- 路径
    - 决定路径， 总是g根目录开始
    - 相对路径，基本以当前环境未开始的一个相对地方     
  
  
#os 
-    值部分
-os.curdir:current dir  当前目录
-os.pardir:parent dr 父亲目录
-os sep 当前系统的路径分隔符
-os.linesep 当前系统的路径分隔符
-os.name 当前的系统名称


#归档和压缩
- 归档。 把多个文件或者文件夹合并到一个文件当中
- 压缩 用算法把多个文件或者文件夹无损或者有损合并到一个文件中

#zip压缩包

#random
- 随机数
- 所有随机模块都是伪随机
- choise() 随机抽取其中一个
- shuttle 打乱顺序列表
#math
             
                           