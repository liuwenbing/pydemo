# OOp-Python面向对象

- Python的面向对象
- 面向对象编程
    - 基础
    - 公有私有
    - 继承
    - 组合 minx
- 魔法函数
    - 魔法函数的概述
    - 构造函数魔法函数
    - 运算类魔法函数
        
# 1 面向对象描述（ObjectOriented，oo）
- oop思想
    - 接触到任意一个任务，首先想到的是任务世界的构成，由模型构成
- 几个名词
    -  oo:面向对象
    -  ooa:***分析
    -  。。。。。
    - 

# 2. 类和对象的概念
- 实例话类
    变量 = 类名（）
    
    obj.成员属性
    obj.方法
- 可以通过内置变量检查类的成员变量和方法
     - 对象的所有成员 obj__dict__ 
     - 类的所有成员  class_name.__dict__


# 3. annoca 使用
 - conda list
 - conda env list:显示虚拟环境
 - conda create -n xxx python=3.6  ：创建版本为3.6的虚拟环境 名称为xxx
 
 
# 4 类的对象的成员分析
- 类和对象可以存储成员，成员可以归类所有，也可以归对象所有
- 类存储成员时使用的是与类关联的一个对象
- 独享存储成员是存储在当前对象中 
- 对象访问一个成员时，一定使用对象中的成员，尝试访问类的成员，如果有对象只能够有此成员。一定使用对象中的成员
- 创建对象的时候，，类中的成员不会放入对象中，而是得到一个空的对象，没有成员
- 通过对象 对类中成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员

# 5 关于self
- self在对象的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数中
- self 本身不是关键字，只是一个接受对象的普通参数，理论上可以用任意一个变量代替
- 当法中有self形参的方法称为非绑定的方法,可以接受对象访问，没有self的是绑定类的方法，只能通过类访问
- 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过__class__  成员来访问
# 6 面向对象特性
- 继承
- 封装
- 多态


 