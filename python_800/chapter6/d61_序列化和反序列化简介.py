"""
1、什么是序列化？
序列化是指把 内存的数据类型 转化为一个 特定格式的内容，该格式的内容可用于存储或者传输给其他平台使用
序列化：
内存中的数据类型-------->序列化-------> 特定的格式 (json格式或者pickle格式)

反序列化：
内存中的数据类型<-------->反序列化<------- 特定的格式 (json格式或者pickle格式)

"""

import json

# python内置数据类型进行序列化json,同时将序列化的写进文件，复杂方法
json_res = json.dumps([11, 'abc', True, False])
print(json_res, type(json_res))
with open('a.txt', mode='wt', encoding='utf-8') as f:
	f.write(json_res)

# 反序列化,将json格式的数据类型，反序列化为python内置的数据类型,复杂方法
str_l = json.loads(json_res)
print(str_l, type(str_l))
print('===============================================================>')


with open('a.txt', mode='rt', encoding='utf-8') as f:
	res1 = json.loads(f.read())
	print(res1, type(res1))

# 如果我们想要保留中文字符串，可以使用json.dumps()函数的ensure_ascii参数。该参数默认为True，
# 表示将所有的非ASCII字符转换成unicode编码。如果我们将该参数设置为False，就可以保留中文字符串了
res_js = json.dumps({'name': '方程杨', 'hobby': '打球'}, ensure_ascii=False)
print(res_js, type(res_js))
