import json

# python内置数据类型进行序列化json,同时将序列化的写进文件，简单方法
l1 = [112, 'abc', True, False]
with open('b.txt', mode='wt', encoding='utf-8') as f:
	json.dump(l1, f)

# 反序列化,将json格式的数据类型，反序列化为python内置的数据类型,简单方法
with open('b.txt', mode='rt', encoding='utf-8') as f:
	res = json.load(f)
	print(res, type(res))