#结构化文件存储
- 保留字符处理
- 把保留字符的部分放在CDATA  块内，CDATA块把部分内部信息视为不需要转义

 - <![CDATA[
    SELECT name ,age
    from sye
    where age>19
    ]]>
- 需要的转义的保留字符和相对应实体引用
    - &： &amp;
    - <： &lt;
    -...一共5个都是以&开头分号结尾
    
        
- 命名空间
    - 为了防止命名冲突
    
        <School>
            <name>err</name>
            <age>19</age>
        </School> 
- 为了避免冲突，需要给可能冲突元素添加命名空间
- xmlns: xml name space

# xml访问
# xml读取 sax dom
- sax 
    - 基于事件驱动的API
    - 利用sax解析文档设计到解析器和事件处理两个部分
    - 特点
        - 快
        - 流式读取
        
- dom
    - 是w3c归定的xml编程接口
    - 一个xml文件在缓冲中以树形结构保存，读取
    - 用途
        - 定位浏览xml任何一个节点信息
        - 添加删除相应的内容
    - mindom
        - mindom.parse(filename)
        - doc.docmentElement()
        - node.getAttribute()
        - node.childNodes() 
        - node.firstNode()
        - node.attribute(tagname)          
    - etree  
        - root.getiterator(filename)
        - root.iter
        - find
        - root.findAll(node_name)
        - node.tag()
        - node.text
        - node.attrib
- xml写入
- 更改
    - ele.set   修改
    - ele.append  添加子元素
    - ele.remove
- 生成创建







        