import requests
url = 'http://www.baidu.com'
# encoding方法的两个作用：
# 1、获取请求编码；
# 2、设置响应编码
# headers:
# 1、获取响应头信息

r = requests.get(url=url)
# 查看默认请求编码
print(f'默认请求编码：{r.encoding}')
print(f'没用设置响应编码：{r.text}')

# 设置响应编码
r.encoding='utf-8'
print(f'设置响应编码之后：{r.text}')

print('*************************************************************')
# 查看响应信息头，提示：headers信息比较重要 (项目工作中一般服务器返回的token/session相关信息都在headers中)
print(r.headers)


















