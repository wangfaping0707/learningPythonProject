import requests
"""
requests模块之post参数data和json的区别:
post请求报文中既可以传data，也可以传json。并且data与json既可以是str类型，也可以是dict类型
二、参数规则

看看json与data的参数规则
2.1 json参数

    使用json参数，报文是dict类型
    如果不指定content-type时，默认为application/json
    使用json参数，报文是str类型
    如果不指定content-type时，默认为application/json

2.2 data参数

    使用data参数，报文是dict类型
    如果不指定headers中content-type的类型，默认application/x-www-form-urlencoded
    相当于普通form表单提交的形式，将表单内的数据转换成键值对，此时数据可以从request.post里面获取，而request.body的内容则为a=1&b=2的这种键值对形式

    注意：
    即使指定content-type=application/json，request.body的值也是类似于a=1&b=2，所以并不能用json.loads(request.body.decode())得到想要的值
    
使用data参数，报文是str类型
如果不指定headers中content-type的类型，默认application/json
综上所述，两种参数的使用情况：

    用data参数提交数据时，request.body的内容则为a=1&b=2的这种形式
    用json参数提交数据时，request.body的内容则为’{“a”: 1, “b”: 2}'的这种形式
    
    
    
    data参数传递的数据格式为表单数据，而json参数传递的数据格式为JSON格式数据。
    在传递数据时，使用data参数需要将数据转换为字典或元组格式，而使用json参数则不需要进行转换。
    此外，使用json参数传递数据时，requests库会自动设置Content-Type头为application/json。

"""


























