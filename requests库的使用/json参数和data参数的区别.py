"""
原文链接：https://blog.csdn.net/weixin_45272371/article/details/129024272
一、关于json:
1、json不是一种数据类型，而是一种数据格式。
2、其实返回的json这个结果（对象），在Python中都把它视为字符串（也就是我们收到的返回数据也全部都是字符串）
假设：
如果我们不把返回的这个字符串转化为字典处理，我们怎么做断言？把一个字符串里面的数据提取出来做断言是多么的困难。
这也就是为什么我们要把返回的json格式的字符串转化为字典的原因。

二、涉及json数据的处理的方法: json字符串和字典之间的转换（json库）
序列化（把字典转换成json格式的字符串），简单讲就是将python的字典转换成json格式字符串，以便进行储存或者传输；我们可以这样记：字符串是有顺序的，所以叫做序列化。
语法：
json.dumps(字典)
json.dumps(字典，indent=None)，indent是空格显示，加入了数值后，可以按照字典的规范写法

反序列化（把json格式的字符串转换成字典），简单讲就是将json格式字符串转换成python字典，用于对其进行分析和处理。
语法：json.loads(json串)

import json

# 序列化成json字符串
d = {'name': 'jod'}
j = json.dumps(d)
print(j)
print(type(j))

# # 反序列化成字典
s=json.loads(j)
print(s)
print(type(s))

注意：而在requests库中，不用json.loads方法进行反序列化，而是提供了响应对象的json方法，用来对json格式的响应体进行反序列化
语法：
r = requests.get(url)
r.json()

三、request请求中注意的问题
如果请求的传参的格式是json
第一种方式：使用data数据格式传入参数

我们之前说了在Python中是没有json这个类型的概念，只有跟json长得像的数据类型（字典），所以需要把字典转化为json格式的字符串。

做法：需要导入json包，使用里面的dumps()函数，把字典进行转换成字符串
import json
dict={'name':'qiuhognji','sex':'男'}
new_json=json.dumps(dict)
response = requests.post(url, headers=headers, params=new_params, data=new_json)
print(reponse.text)
注意：这里的例子其中headers，params参数这些没有用上的可以去掉
举例：这里的例子的接口会不成功，原因是现在的接口改变了，只能记录之前的。
"""
import json
import requests

url = "https://testcentralizedsites.mundossp.com/v1mgmt/test"

# 这里的json.dump()是把字典转化为json格式的字符串。
new_json = json.dumps({
	"MH20220424000001": 1,
	"MH20220424000002": 1
})

headers = {
	'Auth': 'vE6EO5PCIvemJdvk'
}
new_params = {"country": "DE",
              "email": "44001",
              "paypal_email": "0000010",
              "order_id": "879"}
response = requests.request("POST", url, headers=headers, data=new_json)

print(response.text)

"""
注意：
1、如果是post方法，里面又使用了json格式的字符串，那么就要：用data参数传参，首先要把数据类型是字典转换成为json格式的字符串。
2、使用data参数进行数据传递，data参数内部的处理是：内容类型默认是：x-www-form-urlencoded形式传参（也就是表单的形式传参）
解释：
（1）其实我们使用datas参数进行数据传递，其实含义上跟json格式没有一点儿关系，所以在postman中就直接就使用x-www-form-urlencoded形式传参。
（2）我们只是用data参数作为json格式的传载体（意思也就是本来datas不是用来传递json格式的数据，
	但是我们现在硬是要塞进去一个长得像json格式的数据，也就是硬塞了一个字典。但是别人真正需要的是json，
	我塞入字典肯定不合适，那么就要进行数据转化，需要把字典转化为json格式的字符串）
（3）如果使用datas参数进行数据传递，如果内容类型选择的不是x-www-form-urlencoded（也就是其他类型），那么就需要在header中加入content-type


第二种方式：使用json格式传入参数
注意：
1、如果使用这个json格式直接传入数据，那么就不需要数据类型的转换
2、json参数传递数据，本来就是专门为了解决json格式的字符串类型的数据，所以使用json参数时，不需要进行转换。json参数的内部处理机制，就会把字典自动转换为json格式的字符串。
3、json参数传递数据默认的content-type是application/json（因此不需要在headers当中指定content-type）
"""
import requests
url = "https://testcentralizedsites.mundossp.com/v1mgmt/test"
new_json = {
	"MH20220424000001": 1,
	"MH20220424000002": 1
}
headers = {
	'Auth': 'vE6EO5PCIvemJdvk'
}
new_params = {"country": "DE",
              "email": "44001",
              "paypal_email": "0000010",
              "order_id": "879"}
response = requests.request("POST", url, headers=headers, json=new_json)
print(response.text)

"""
requests的请求方法：
1、requests.get(url,param=None) 发起get请求。param是请求参数，是追加在url后面的。字典类型。
2、requests.post(url,data=None,json=None)发起post请求：

data参数：
任意的content-type都可以用参数传参。
不指明content-type的情况下，默认的content-type是x-www-form-urlencoded,且是字典格式。
如果是其他类型的content-type，需要在headers当中，加上content-type类型。

json参数：
给content-type为application/json格式使用的。

字典类型
不需要在header当中指定content-type
以上两个方法，都是使用的requests.request(mothod,url,**kwargs)

"""

















