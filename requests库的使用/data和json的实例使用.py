# post请求中，可以使用data传递参数，也可以使用json传递参数。那么，两种方式有什么区别？

# 1. 如果参数为JSON数据，可以直接传入json参数，它将自动编码并将Content-Type的置为application/json
import requests
import json
payload = {'key1': 'value1', 'key2': 'value2'}
url = 'https://httpbin.org/post'
r = requests.post(url=url, json=payload)
print(r.text)
print('---------------------------------------------------------')

# 如果data传递的参数为字符串，如：json.dumps(payload)，则request对参数进行url编码，Content-Type的值为None，
# 所以data传字符串时，一定要在header中指定Content-Type。
headers = {'Content-Type': 'application/json'}
r1 = requests.post(url=url, headers=headers, data=json.dumps(payload))
print(r1.text)

print('************************************************************************')
# 如果data传递的是字典、元组组成的列表或列表作为值的字典，则request对参数进行url编码，
# Content-Type的值为application/x-www-form-urlencoded。

# 字典
payload1 = {'key1': 'value1', 'key2': 'value2'}
r2 = requests.post(url=url, data=payload1)
print('字典', r2.text)
print('********************************你好****************************************')

# 列表
payload2 = [('key1', 'value1'), ('key2', 'value2')]
r3 = requests.post(url=url, data=payload2)
print('列表', r3.text)

print('*******************************好多好多好多和****************************************')

# 列表作为字典的值
payload3 = {'key1': ['value1', 'value2']}
r4 = requests.post(url=url, data=payload3)
print('列表作为字典的值：', r4.text)








