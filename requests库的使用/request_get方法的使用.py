import requests
'''
1、导入request库；
2、调用requests库的get方法
'''
url = 'http://www.baidu.com'
# 获取相应数据，r为响应对象
r = requests.get(url)
print(type(r))
# 获取请求的url
print(f'获取请求的url：{r.url}')
print(f'获取相应的状态码：{r.status_code}')
# 以文本形式获取响应内容
print(f'以文本形式获取响应内容：{r.text}')

print(r.content)