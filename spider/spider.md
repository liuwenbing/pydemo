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
                                            