#log 
#//yyds/p/6901864.html
- logging
- 包括四大组件
## 1.日志相关概念
- 日志
- 日志的级别
    - 不同的用户关注不同的程序信息
    - debug
    - info
    - notice
    - warninr
    - error
    - critical
    - alter
    - emergrncy
- i/o 不要太频繁
- log作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time 
    - 地点
    - level
    - 内容
- 成熟的第三方日志

# 2。logging模块
- 日志级别
    - 级别可自定义
    - debug
    - info
    - warning
    - error
    - critical
- 初始化/写日志实例需要指定级别，只有高于级别的时候才能被记录下来
- 使用方式
    -直接使用logging（ ）
    