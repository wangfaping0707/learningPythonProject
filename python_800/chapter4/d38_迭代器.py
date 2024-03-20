"""
1、什么是迭代器？
迭代器是指迭代取值的工具，迭代是一个重复的过程，每次重复都是基于上一次的结果而继续的，单纯的重复并不是迭代

2、可迭代对象：只有含有内置方法—__iter__()方法的对象都是可迭代对象

3、可迭代对象调用__iter__()方法就是将自己转换为迭代器对象

"""
l = [1, 2, 3, 4]
l_iterator = l.__iter__()

s = 'hello'
l_iterator = s.__iter__()

t = (11, 22, 33)
t_iterator = t.__iter__()

set1 = {111, 222, 333, 444}
set1_iterator = t.__iter__()

# 文件也是属于可迭代对象
with open('a.txt', mode='a+', encoding='utf-8') as f:
	f.__iter__()
	pass
# 字典
d = {'a': 222, 'b': 4443, 'c': 9834}
d_iterator = d.__iter__()

# 使用迭代器对象遍历字典
while True:
	# d_iterator = d.__iter__()
	try:
		print(d_iterator.__next__())
	except StopIteration:
		break