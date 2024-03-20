import requests

'''
1、请求方法get
2、参数 params：字典或字符串（推荐使用字典）
'''
params = {'id': 1001}
url = 'http://www.baidu.com'

# 1、params参数为字典
r = requests.get(url, params=params)
print(f'请求的url：{r.url}')

# 2、请求参数的值为列表
# params = {'id':[1001, 1002, 1003]}   不推荐这种写法
# 推荐下面这种写法, %2C ASCI值为逗号
params1 = {'id': '1001,1002,1003'}
r1 = requests.get(url, params=params1)
print(f'请求的url：{r1.url}')

# 3、请求参数有多个,多个键值对
params2 = {'id': 1001, 'kw': '上海'}
r2 = requests.get(url,params=params2)
print(f'请求的url：{r2.url}')





