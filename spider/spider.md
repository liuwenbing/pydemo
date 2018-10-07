# 0 爬虫准备工作
- 参考资料
    - python 网络采集，图灵工业出版
    - 精通Python 爬虫框架scrapy 
    - python3网络爬虫 /c406495762/article/details/72858983
    
    
# urllib
- b包含模块
 - urllib.request :打开和读取
 - urllib.error :包含urllib.request产生的常见错误，使用try捕捉
 - urllib.parse 包含URL的方法  
 
- 网页编码的解决
    - chardet  可以自动检测页面的编码格式，可能有误
    
    
- urlopen  的返回对象
    - geturl() 
    - info()     
    - getcode()
    
- request.date的使用
    -get
        - 利用参数给服务器传递信息
        - 参数dict ，然后parse
    -post  
        - 一般向服务器传递参数信息
        - post 是把信息自动加密处理
        - 我们如果想把信息post 需要用到data参数
        - 使用post 意味着http请求可能需要更改
           - content-type appellation/x-www.form-urlencode
           - content-length 数据长度
           - urllib。parse。urlencode可以将字符转化为上面的
        - 为了更多的请求信息，单纯的通过urlopen函数已经不太好用来
        - 需要利用request。Request
        
- urllib.error
    -  UrkError 
        - 没网
        - 服务器连接失败
    - httpError     ,是       UrlError      子类
    
    - 两者区别
        - httperror 是请求的返回状态吗错误，400以上的状态吗
        - UrlError对应的一般是网络出现的错误
        - oserror->UrlError->httperror 
- useragent
    - useragent : 用户代理，属于heads的一部分，服务器通过它来判断访问者部分           
- proxyHandler处理 （代理服务器）
    - 使用IP代理，是爬虫的常用手段
    - 获取代理服务器的地址
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理来隐藏真实访问中，代理也不允许频繁访问某一个固定的网站，所以，代理一定要很多很多的
    - 基本使用步骤
        - 设置代理地址
        - 创建    proxyHandler
        
        
- cookie & session
    - 由于http协议的无记忆性，人们为了祢补这个缺憾，所以采用补充协议
    - cookie是发给用户的一段嘻嘻，session是保存在服务器上对应的另一半信息，用来记录用户信息
    
-cookie session区别
    - 存放位置不同
    - cookie不安全
    - session 会保存在服务器上一段时间，会过期
    - 半个cookie 保存数据不超过4k，很多浏览器限制最多保存20个 
- session 的存放位置
    - 存在服务器
    - 一般情况，session 放在内存中或者数据库中
- 使用cookie登录
    - 直接把cookie复制下来，然后手动请求头
    - http模块 包含一些cookie的模块，
        - cookiejar
        - 
 - cookie作为一个变量，打印出来
    - name：名称
    - domain：可以访问的域名
    - value：值
    - path：可以访问cookie 的页面路径
    - exprise 过期时间
    - size：大小
    - http字段              
- cookie 的保存-fileCookieJar
- cookie的读取

- ssl
    - ssl证书就是遵守ssl安全套阶层协议服务器数字证书
    - 美国网景公司开发
    - ca机构
    
    
- js加密
    - 有的翻爬虫策略采用js，需要传输的数据进行加密处理
    - 经过加密，传输的就是密文，但是加密函数或者过程一定是在浏览器完成，也就是把一段代码暴露出来
    - 通过阅读加密算法，也就可以模拟出加密啊过程，从而达到破解
    - 过程参考案例v13
    
    
- ajax
    - 异步请求
    - 一定会有json
    
    
# Requests -         献给人类
-继承来urllib 的所有特征
-底层是urllib3
- 中文文档
-   安装 
    - conda install charset 
- 请求
    - get
        - requests.get(url)
        - requests.request("get",url)
        - 可以带有headers params
        
        
    - get  返回内容
        - v15        
- post 
    - rsp = requests.post(url,data=data)
    - data  headers  要求dict类型
    
    
- proxy 
    - proxies= {
        "http":""
        "https":""
        }
      rsp = requests.request("get",http:'.....)  
      
      
      
- 用户验证
    - 代理验证 
        - 可能需要使用http basic auth
        - 用户名：密码@代理地址： 端口地址
        
- cookie 
    - requests 可以自动处理cookie信息
        rsp = requests.get(url)
        
        cookirjar = rsp.cookies
        
        cookiedir = requests.utils.dict_from_cookiejars(cookiejar)
        
        
        
- session
    - 跟服务器端session 不是一个
    - 模拟一次会话，从客户端浏览器连接开始，到客户端浏览器断开
    - 让我们跨请求保持某些参数，比如在同一个session 实例出发，所以请求之间保持cookie
    
    
    
    
# 页面解析和数据提取
    - 结构数据  ： 先有结构，在有数据
        - json文件
            - jsonpath
            - 转换为python类型的操作
        - xml文件
            - 转化为python 类型
            - xpath
            - 正则
            - css 选择器             
    - 非结构化数据 ：先有数据，在有结构
        - 文本
        - 电话号码，邮箱地址
        - 通常处理此类数据，使用正则表达式
    - Html文件
        - 正则
        - xpath
        - css 选择器    
        
## 正则表达式
- v18  match的使用
- 正常使用规则
    - match    开始位置找，一次匹配
    - search   任何位置找，一次匹配  v19
    - findall  全部匹配，返回列表
    - split    分割字符串，返回列表
    - sub      替 换
                
- 匹配中文
    - 中文unicode 范围主要[u4e00-u9fa5]
    - v20
    - 贪婪 非贪婪
    - 贪婪 尽可能多的匹配
    - 默认贪婪 
         - 文本 abbbbbcc
         -贪婪  abbbb
         非贪婪  ab        
         
# xml 
- xml


# Beautifulsoup

- tag 
    - 对应html中的标签
    - 可以通过soup，tag_name
    - tag的两个重要属性
        - name
        - attrs
        案例22
        
- nav

- beautifulsoup
    - 表示文档的内容，大部分可以把它当作是tag对象
    - 一般我们可以用soup 来表示
- comment
    - 特殊类型的nav对象
    - 对其输出，则内容不包括注释
- 遍历文档对象
    - contents ：tag的子节点以列表的方式输出
    - children ：子节点以迭代器返回
    - descendants ：所有子孙
    - string
    - v23
-  搜索文档对象
    - find_all
    - name
    - 按照那个字符串搜索，可以传入内容
        - 字符串
        - 正则表达式
        - 列表
        
        
        
- css 选择器
    - 使用soup.select, 返回一个列表
    - 通过标签名称，soup.select("title")
    - 通过类名  soup.select(".title") 
    - ...㩐
    -                
    
    
- 正则表达式
   
   
   
# 动态html
## 爬虫跟反爬虫
- JavaScript
- JQuery
- Ajax
- DHTML
- PYhon 采集动态数据
    - 从Javascript 代码入手数据
    - python 第三方库运行javascript，直接采集浏览器看到的页面
    
## selenium + phantomJs
- selenium :web 自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
- phantomJs
    - 基于webkit的无界面的浏览器
-  selenium 库 又一个WebDriver 的API
-  案例v25   
- selenium 操作
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - ...
        -  
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 案例v26 
        
        
# 验证码
    - 图片
    - 极验
    - 12306
    
    
# scrapy
# 爬虫框架
- 框架
   - scrapy
   - pyspider
   - crawley
   
- scrapy
    - 中文网站
- scrapy 概述
    - 包含各种邮件
        - ScrapyEngine ：神经中区，大脑，核心
        - Scheduler :引擎发来的request 请求，调度器需要处理，然后交换引擎
        - Download下载器 ： 把引擎发来的  requests 发出请求，得到response
        - spider 爬虫： 负责把下载器得到的网页/结果进行分解，分解成数据+链接
        - ItemPipeline 管道： 详细处理item
        - DownloaderMiddleware 下载中间件： 自定义下载的功能扩展
- 爬虫项目大概流程
    - 新建项目 scrapy startproject   XXX
    - 明确需要的目标/产出 编写item。py
    - 制作爬虫 ：地址spider/xxspider.py
    - 存储内容 ： pipelines.py
    
    
- ItemPipeline
    - 爬虫提取出数据存入item后，item 中保存的数据需要进一步处理，比如清洗，去重，，存储等
    -   pipeline 需要处理process_item函数
    - process_item：
        - spider 提取出item 作为参数处理，同时传入的还是有spider
        - 此方法必须实现
        - 必须返回一个item，被丢弃的item不会被之后的pipeline 处理
    - init ：构造函数
        - 进行一些必要函数的初始化
        - open_spider 对象被开启的时候调用
        - close_spider 当spider对象关闭的时候调用


- spider 
    -  对应的是文件夹spiders下文件
    - __init__ 初始化爬虫名称，start_urls
    - start_requests 生成  requests对象交给scrapy  下载并返回respond
    - parse 根据返回的response 解析出现相应的item。item自动进入pipeline ；如果需要，解析出url
        URL自动交给  requests模块，一直循环下去
        
    - name： 设置爬虫名称
    - start_urls ：设置开始的第一批爬去url
    - allow_domains:spider 允许爬去的域名列表
    - start_requests（self） ：只被调用一次
    - log  ：日志记录
    - parse
    
- 中间件 
 - 中间件是处于引擎和下载器中间的一层组件
 - 可以有很多个，被按顺序加载
 - 作用是对发出请求和返回的结果进行预处理
 - 在middle wares文件中
 - 需要settings 中设置生效
 - 一般一个中间件完成一些功能 
 - 必须实现 一下一个或者多个
    - process_requests (self,request,spider)
    - 必须返回none 或者  response。。。
    - 
    
    
- 去重
    - 为了防止爬虫进入死循环。需要去重
    - 即在spider 中 的parse 函数中，返回  request 的时候加上dont_filter= false
        
        
- 如何使用spider 使用selenium
    - 可以放入中间件 process_request
    - 在函数中调用selenium ，完成爬取后返回  response
# scrapy-shell
    - scrapy shell "XXXXx"
 - response
    - 爬取到的内容保存在  response 中 
    - response.body 是网页的代码
    - response。headers 是返回的http 的头信息
    -   response。xpath 允许使用，
    -   response。css（）
    
-  selector
    - 选择器，允许用户使用选择器来选择自己想要的内容
    -   response .selector .xpath:response.xpath 是 selector.xpath 的快捷方式
    - response.selector.css : response.css 是他的快捷方式
    - selector.extract : 把节点的内容用unicode 形式返回
    - selector.re : 允许用户通过正则选取内容
               
# 分布式爬虫
    - 单机爬虫的问题
        - 单机的效率低
        - io吞吐量
    - 多爬虫问题
        - 数据共享
        - 在空间上不同的多台机器，可以成为分布式
- 需要做：
    -                                                                                                       